# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth import models as auth_models
from django.utils import timezone


class UserProfile(auth_models.AbstractUser):
    address = models.TextField("Adres", blank=True, null=True)
    phone = models.CharField("Telefon numarası", max_length=20, blank=True, null=True)
    company = models.CharField(
        "Çalıştığı şirket",
        blank=True,
        null=True,
        help_text="Kamu çalışanları bağlı oldukları müdürlüğü yazabilir.",
        max_length=255
    )
    public_officer = models.NullBooleanField("Kamu çalışanı", default=False, blank=True, null=True)
    role = models.CharField("Bağlı olunan departman/bölüm", blank=True, null=True, max_length=255)
    birthdate = models.DateField("Doğum tarihi", blank=True, null=True)
    lkd_id = models.CharField("LKD üye numarası", blank=True, null=True, max_length=32)
    inetd_id = models.CharField("INETD üye numarası", blank=True, null=True, max_length=32)
    github_username = models.CharField("Github kullanıcı adı", max_length=64, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.username)

    class Meta:
        verbose_name = "Kullanıcı profili"
        verbose_name_plural = "Kullanıcı profilleri"


class AdministrativeNote(models.Model):
    user = models.ForeignKey(UserProfile, related_name="notted_user")
    adder = models.ForeignKey(UserProfile, related_name="adder")
    note = models.TextField("Not")
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return smart_unicode("{0} #{1}".format(self.get_full_name(), self.id))

    class Meta:
        db_table = "administrative_notes"
        verbose_name = "Yönetimsel not"
        verbose_name_plural = "Yönetimsel notlar"

