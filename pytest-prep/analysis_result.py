def validate_analysis_result(golden_dataset_client, study_id, computed_ffr_value, tolerance=0.05):
    golden_value = golden_dataset_client.get_reference_value(study_id)
    difference = abs(computed_ffr_value - golden_value)
    if difference <= tolerance:
        return {"status": "pass", "study_id": study_id, "difference": difference}
    return {"status": "fail", "study_id": study_id, "difference": difference}
