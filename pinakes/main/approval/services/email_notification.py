"""Email notification for an approval request"""
import logging
import string
from importlib.resources import read_text
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend

from pinakes.common.auth.keycloak_django.clients import get_admin_client

logger = logging.getLogger("catalog")


class EmailNotification:
    """Service class for email notification"""

    def __init__(self, request):
        self.request = request

    def process(self):
        """process the service"""
        self._send_mail()
        return self

    def _send_mail(self):
        settings = self.request.workflow.template.process_method.settings
        sender = settings.pop("from", None)
        security = settings.pop("security", None)
        if security:
            settings[security] = True
        backend = EmailBackend(**settings)

        group_id = self.request.group_ref
        approvers = get_admin_client().list_group_members(group_id, 0, 100)
        for approver in approvers:
            logger.info("Sending email to %s", approver.email)
            send_mail(
                subject=self._subject(),
                message=self._plain_body(),
                html_message=self._html_body(approver),
                from_email=sender,
                recipient_list=(approver.email,),
                connection=backend,
            )
        backend.close()

    def _subject(self):
        return (
            f"Catalog:Approval Order {self.request.id}: "
            f"{self.request.requester_name}"
        )

    def _plain_body(self):
        return (
            "There is a Pinakes order requires your approval. "
            f"Please visit {self._web_url()}/{self._approval_link()}."
        )

    def _html_body(self, approver):
        content = self.request.request_context.content
        params = {
            "approval_id": self.request.id,
            "approver_name": f"{approver.firstName} {approver.lastName}",
            "orderer_email": self.request.user.email,
            "requester_name": self.request.requester_name,
            "order_id": content["order_id"],
            "order_date": self.request.created_at.strftime("%m/%d/%Y"),
            "order_time": self.request.created_at.strftime("%H:%M:%S"),
            "product": content["product"],
            "portfolio": content["portfolio"],
            "platform": content["platform"],
            "approve_link": self._approval_link(),
            "web_url": self._web_url(),
        }
        email_template = read_text("pinakes.data", "email_template.html")
        return string.Template(email_template).safe_substitute(**params)

    def _web_url(self):
        return self.request.request_context.context.get(
            "http_host", "localhost"
        )

    def _approval_link(self):
        return f"ui/catalog/approval/request?request={self.request.id}"
