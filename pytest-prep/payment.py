# payment.py
class ValidationError(Exception):
    pass


def process_payment(payment_gateway, order_id, amount):
    try:
        result = payment_gateway.charge(order_id, amount)
    except ConnectionError:
        return {"status": "failed", "reason": "gateway_unavailable", "order_id": order_id}
    except ValidationError as e:
        return {"status": "failed", "reason": "invalid_request", "order_id": order_id, "detail": str(e)}

    if result["success"]:
        return {"status": "completed", "order_id": order_id}
    return {"status": "declined", "order_id": order_id}
