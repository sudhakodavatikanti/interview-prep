from unittest.mock import Mock
from study_results import process_study_batch
import pytest



"""
1. study-id not found in study_service  - status error
2. ffr_val < 0 for a study_id - status invalid
3. ffr_val <= threshold - status flagged
4. ffr_val > threshold - status normal
5. ffr-vale == threshold - status flagged
"""


@pytest.fixture
def study_service_mock():
    return Mock()

def test_study_results_invalid(study_service_mock):
    

    study_service_mock.fetch_study.return_value = {'study_id': ['study-123'], 'ffr_value': -2} 
    result = process_study_batch(study_service_mock, ['study-123'])
    assert result == [{"study_id": 'study-123', "status": "invalid"}]


def test_study_results_flagged(study_service_mock):
    
    study_service_mock.fetch_study.return_value = {'study_id': ['study-456'], 'ffr_value': 0.8} 
    result = process_study_batch(study_service_mock, ['study-456'])
    assert result == [{"study_id": 'study-456', "status": "flagged"}]


def test_study_results_flagged_another(study_service_mock):

    study_service_mock.fetch_study.return_value = {'study_id': ['study-46'], 'ffr_value': 1.0} 
    result = process_study_batch(study_service_mock, ['study-46'])
    assert result == [{"study_id": 'study-46', "status": "flagged"}]


def test_study_results_normal(study_service_mock):

    study_service_mock.fetch_study.return_value = {'study_id': ['study-6'], 'ffr_value': 2} 
    result = process_study_batch(study_service_mock, ['study-6'])
    assert result == [{"study_id": 'study-6', "status": "normal"}]

def test_study_results_error(study_service_mock):
    

    study_service_mock.fetch_study.side_effect = Exception("fetch failed")
    result = process_study_batch(study_service_mock, ['study-6'])
    assert result == [{"study_id": 'study-6', "status": "error"}]


def test_study_results_empty_list(study_service_mock):
    
    result = process_study_batch(study_service_mock, [])

    assert result == []

