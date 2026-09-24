def process_study_batch(study_service, study_ids, ffr_threshold=1.0):
    results = []
    for study_id in study_ids:
        try:
            study_data = study_service.fetch_study(study_id)
        except Exception:
            results.append({"study_id": study_id, "status": "error"})
            continue

        if study_data["ffr_value"] < 0:
            results.append({"study_id": study_id, "status": "invalid"})
        elif study_data["ffr_value"] <= ffr_threshold:
            results.append({"study_id": study_id, "status": "flagged"})
        else:
            results.append({"study_id": study_id, "status": "normal"})

    return results
