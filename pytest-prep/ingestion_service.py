def check_ingestion_status(ingestion_service, study_id, expected_series_count):
    series_list = ingestion_service.get_series(study_id)
    if len(series_list) == 0:
        return {"study_id": study_id, "status": "not_found"}
    if len(series_list) < expected_series_count:
        return {"study_id": study_id, "status": "incomplete", "received": len(series_list)}
    return {"study_id": study_id, "status": "complete", "received": len(series_list)}
