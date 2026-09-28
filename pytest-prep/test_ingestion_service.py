from ingestion_service import check_ingestion_status
import pytest





"""
1. len(series_list) === 0 , return status not found
2. len(series_list) < expected, return status incomplete and len(series_list)
3. len(series_list) >= expected, return status complete and len(series_list)
"""

def test_series_list_not_found(mock_service):

    mock_service.get_series.return_value = []
    result = check_ingestion_status(mock_service, 'study_123', 5)
    assert result == {'study_id': 'study_123', 'status': 'not_found'}