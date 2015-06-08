# coding: utf-8

from __future__ import unicode_literals

APPROVE_APPLICATION_EMAIL_TEMPLATE = "course-approved"
REJECT_APPLICATION_EMAIL_TEMPLATE = "course-rejected"

MAIL_TEMPLATES = (
    (APPROVE_APPLICATION_EMAIL_TEMPLATE, "Application Approved"),
    (REJECT_APPLICATION_EMAIL_TEMPLATE, "Application Rejected"),
)

MAIL_SUBJECT_APPROVE_APPLICATION = "Başvurunuz kabul edildi"
MAIL_SUBJECT_REJECT_APPLICATION = "Başvurunuz kabul edilmedi."
