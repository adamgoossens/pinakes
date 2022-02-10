import pytest

from automation_services_catalog.main.approval.tests.factories import (
    ActionFactory,
)
from automation_services_catalog.main.approval.models import Action


class TestAction:
    @pytest.mark.django_db
    def test_action(self):
        action = ActionFactory()
        assert action.operation == Action.Operation.MEMO

    @pytest.mark.django_db
    def test_action_operation(self):
        action = ActionFactory(operation="bad")
        assert action.operation == "bad"  # TODO: why allow any string?
