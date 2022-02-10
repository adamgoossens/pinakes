""" Test module for starting an OrderItem """
from unittest.mock import Mock
from unittest.mock import patch
import pytest
from automation_services_catalog.main.catalog.tests.factories import (
    OrderItemFactory,
)
from automation_services_catalog.main.catalog.models import OrderItem
from automation_services_catalog.main.catalog.services.provision_order_item import (
    ProvisionOrderItem,
)


@patch(
    "automation_services_catalog.main.catalog.services.provision_order_item.StartTowerJob",
    autoSpec=True,
)
@pytest.mark.django_db
def test_provision_order_item(mock):
    """Test starting an order item"""
    order_item = OrderItemFactory()
    svc = Mock()
    svc.job.id = "abcdef"
    mock.return_value.process.return_value = svc
    ProvisionOrderItem(order_item).process()
    order_item.refresh_from_db()
    assert order_item.state == OrderItem.State.ORDERED
    assert order_item.inventory_task_ref == svc.job.id
