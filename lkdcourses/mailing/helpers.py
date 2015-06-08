from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.conf import settings

from .models import MailLog


def send_email_from_template(to_profile, template_name, global_merge_vars=None, merge_vars=None, from_name=None, from_email=None, subject=None, sent_before_control=False):

    log_type = template_name

    if sent_before_control:
        if mail_is_sent_before(to_profile, log_type):
            return False

    if to_profile.mail_subscription is False:
        return False

    msg = EmailMessage(
        to=[to_profile.email, ]
    )

    msg.template_name = template_name

    if not global_merge_vars:
        global_merge_vars = {}

    msg.global_merge_vars = global_merge_vars

    if merge_vars:
        msg.merge_vars = merge_vars

    msg.subject = subject

    if not from_email:
        from_email = settings.MAILING_FROM_EMAIL

    if not from_name:
        from_name = settings.MAILING_FROM_NAME

    msg.from_email = from_email
    msg.from_name = from_name

    msg.send()

    mandrill_id, mandrill_status = "-1", "unknown"
    try:
        if msg.mandrill_response and len(msg.mandrill_response):
            mandrill_id, mandrill_status = msg.mandrill_response[0].get("_id"), msg.mandrill_response[0].get("status")
    except Exception as error:
        pass

    mail_log = MailLog(
        to=to_profile,
        type=log_type,
        mandrill_response_id=mandrill_id,
        mandrill_status=mandrill_status,
    )

    mail_log.save()


def mail_is_sent_before(to_profile, template_name):
    return MailLog.objects.filter(to=to_profile, type=template_name).count() > 0
