from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from .constants import MAIL_TEMPLATES


class MailLog(models.Model):
    to = models.ForeignKey("profiles.UserProfile", related_name="mail_profile")
    type = models.CharField(choices=MAIL_TEMPLATES, max_length=32)
    sent_at = models.DateTimeField(default=timezone.now)
    mandrill_response_id = models.CharField(max_length=255, null=True, blank=True)
    mandrill_status = models.CharField(max_length=255, null=True, blank=True)
