# -*- coding: utf-8 -*-


from django.db import models
from django.utils.encoding import smart_unicode

from .constants import *


class Venue(models.Model):
    name = models.CharField("Etkinliğin yapılacağı alanın adı", max_length=255)
    address = models.TextField("Alanın adresi")
    directions = models.TextField("Alana ulaşım için yönlendirmeler")
    accommodation = models.TextField("Konaklama ile ilgili bilgiler.")
    latitude = models.DecimalField(max_digits=6, decimal_places=3, help_text="Harita gösterimi için gerekli.")
    longitude = models.DecimalField(max_digits=6, decimal_places=3, help_text="Harita gösterimi için gerekli.")

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        db_table = 'venues'
        verbose_name = "Etkinlik alanı"
        verbose_name_plural = "Etkinlik alanları"


class Sponsor(models.Model):
    name = models.CharField("Sponsor ismi", max_length=255)
    url = models.CharField("Sponsor adres", max_length=255)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        db_table = "sponsors"
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsorlar"


class Event(models.Model):
    name = models.CharField("Etkinlik adı", max_length=255)
    slug = models.SlugField()
    cover_image = models.ImageField(upload_to="event_cover_images")
    start_date = models.DateField("Başlangıç tarihi")
    end_date = models.DateField("Bitiş tarihi")
    allowed_course_count = models.IntegerField(
        "Tek bir kişinin başvuru yapabileceği kurs sayısı",
        help_text="Biri asil, diğerleri yedek olmak üzere toplam.",
        default=2,
    )
    faq = models.TextField("Sıkça sorulan sorular")
    venue = models.ForeignKey(Venue)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        db_table = 'events'
        verbose_name = "Etkinlik"
        verbose_name_plural = "Etkinlikler"


class EventSponsor(models.Model):
    event = models.ForeignKey(Event)
    sponsor = models.ForeignKey(Sponsor)
    type = models.IntegerField(choices=SPONSOR_TYPES)

    def __unicode__(self):
        return smart_unicode("{0} - {1}".format(self.event, self.sponsor))

    class Meta:
        db_table = "event_sponsors"
        verbose_name = "Etkinlik sponsoru"
        verbose_name_plural = "Etkinlik sponsorları"