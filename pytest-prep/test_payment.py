import logging
from unittest.mock import Mock
from payment import process_payment
from payment import ValidationError

logger = logging.getLogger(__name__)


def test_process_payment_success():
    mock_gateway = Mock()
    mock_gateway.charge.return_value = {"success": True}

    result = process_payment(mock_gateway, order_id=123, amount=50.00)

    assert result == {"status": "completed", "order_id": 123}
    mock_gateway.charge.assert_called_once_with(123, 50.00)


def test_process_payment_declined():
    mock_gateway = Mock()
    mock_gateway.charge.return_value = {"success": False}

    result = process_payment(mock_gateway, order_id=456, amount=30.00)

    assert result == {"status": "declined", "order_id": 456}


def test_process_payment_gateway_raises_exception():
    mock_gateway = Mock()
    mock_gateway.charge.side_effect = ConnectionError("Gateway timeout")

    result = process_payment(mock_gateway, order_id=789, amount=20.00)
    logger.info("result: %s", result)

    assert result == {"status": "failed",  "reason": "gateway_unavailable", "order_id": 789}


def test_process_payment_validation_raises_exception():
    mock_gateway = Mock()
    mock_gateway.charge.side_effect = ValidationError("amount does not match order total")

    result = process_payment(mock_gateway, order_id=931, amount=1.00)
    logger.info("result: %s", result)

    assert result == {"status": "failed", "reason": "invalid_request", "order_id": 931, "detail": "amount does not match order total"}

