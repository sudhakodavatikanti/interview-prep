import pytest
from unittest.mock import Mock
from analysis_result import validate_analysis_result


def test_analysis_result_success():
    golden_dataset_client_mock = Mock()

    golden_dataset_client_mock.get_reference_value.return_value = 0.75

    result = validate_analysis_result(golden_dataset_client_mock, 'study-1', 0.78, 0.05)

    assert result == {"status": "pass", "study_id": 'study-1', "difference": pytest.approx(0.03)}






   
