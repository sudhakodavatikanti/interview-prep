Q: You mentioned you own a nightly regression suite with about 1,200 tests. Walk me through how you'd design the system that runs it — assume it needs to finish within a fixed overnight window, handle some tests being flaky, and produce a report the team can act on each morning. How would you architect this?

1. Clarify scale and constraints first: 1,200 tests, fixed overnight window, some tests are flaky, need an actionable report by morning. That scale tells me I need real parallelization, not just a single sequential run.

2. High-level architecture — five components:

Orchestrator/scheduler — owns the run. Breaks the 1,200 tests into individual work items (ideally one task per test, or small batches) and pushes them onto a queue for this specific run_id.
Broker (Redis or RabbitMQ, managed via Celery) — the message transport. Holds the queue of pending tasks; its only job is getting work to an available worker.
Worker pool — pulls one task at a time off the queue, executes that single test, and immediately writes the result — not held in memory until the batch finishes.
Result store (a real database, e.g. Postgres) — the system of record. Every write is keyed by (run_id, test_id), not by worker, so results survive regardless of which worker produced them or whether that worker later dies. I wouldn't rely on Celery's Redis result backend for this — Redis is transient; durable, queryable history belongs in a real database.
Reporter/notifier — once every task for the run_id has resolved, aggregates results into an HTML report (Playwright's built-in report works well) and pushes a Slack notification for visibility.
3. Parallelization / distribution: shard the 1,200 tests across available workers — for example, splitting by dataset if tests are grouped that way. (Worth naming as a known limitation: static splits can cause load imbalance if some shards are slower; a dynamic work-queue where idle workers just pull the next available task self-balances better than a fixed upfront split.)

4. Failure handling — the core distributed-systems piece: track status per (run_id, test_id), with distinct states for two different triggers that must not be conflated:

Normal path: queued → running → completed (result written, pass/fail recorded).
Worker failure (crash, OOM, instance reclaimed): the task was never acknowledged as done. The broker's visibility-timeout mechanism detects this and automatically requeues that single task to another worker. Because tracking is per-test, only the handful of tasks truly mid-flight at the moment of failure are affected — everything already completed and written to the database is untouched.
Deliberate cancellation (a user stops the run): a separate state. Cancelled tasks must not be retried or redispatched — that's the opposite of a worker failure, and treating them the same would cause a cancelled run to keep rescheduling tests the user explicitly asked to stop.
Writes to the result store should be idempotent (keyed by run_id + test_id), since a task can occasionally get redelivered to two workers if one is merely slow rather than truly dead.
5. Flaky test handling: rerun failing tests up to 3x automatically. If a test fails at the exact same point every time, treat that as a signal of a real bug or timing issue (missing wait, race condition) rather than flakiness — don't just blanket-retry everything into a false pass.

6. Reporting: once all tasks for the run resolve (completed, retried-and-resolved, or cancelled), generate the HTML report and post it with a Slack notification so the team can act on it first thing in the morning.

Why this design holds up: per-test tracking plus a durable result store is exactly what makes "no result loss under failure" and "safe mid-run cancellation" achievable without fragile custom recovery code — both fall out naturally from tracking work at the right granularity.



