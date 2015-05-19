# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_unicode


class Instructor(models.Model):
    fullname = models.CharField("ad soyad", max_length=255)
    avatar = models.ImageField(upload_to="instructor_avatars", blank=True, null=True)
    about_text = models.TextField("Eğitmen hakkında", null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.fullname)

    class Meta:
        db_table = "instructors"
        verbose_name = "Eğitmen"
        verbose_name_plural = "Eğitmenler"


class Course(models.Model):
    event = models.ForeignKey("events.Event")
    name = models.CharField("Kurs ismi", max_length=255)
    description = models.TextField("Kurs açıklaması", blank=True, null=True)
    slug = models.SlugField()
    start_date = models.DateField("Başlangıç tarihi")
    end_date = models.DateField("Bitiş tarihi")
    participation_rules = models.TextField(
        "Katılım koşulları",
        help_text="Bir boşluk bırakarak maddeler halinde yazınız.",
    )
    covered_topics = models.TextField(
        "Konular",
        help_text="Bir boşluk bırakarak maddeler halinde yazınız.",
    )
    instructors = models.ManyToManyField(Instructor)
    deadline_date = models.DateField("Son başvuru ekleme/düzenleme tarihi")
    quota = models.IntegerField("Katılımcı kotası", blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        db_table = "courses"
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class UserChoice(models.Model):
    """
    One user may apply more than one courses with priority. If they didn't get acception from the course instructors,
    their application is valid for lower priority courses.
    """

    user = models.ForeignKey("profiles.UserProfile")
    event = models.ForeignKey("events.Event")
    course = models.ForeignKey(Course)
    priority = models.IntegerField("Öncelik")  # [1-N]

    def __unicode__(self):
        return smart_unicode("{0} - {1} - {2}".format(self.event, self.event, self.priority))

    class Meta:
        db_table = 'user_choices'
        verbose_name = 'kullanıcı kurs seçimi'
        verbose_name_plural = 'kullanıcı kurs seçimleri'


class Application(models.Model):
    user = models.ForeignKey("profiles.UserProfile", related_name="application_user")
    event = models.ForeignKey("events.Event")
    choices = models.ManyToManyField(UserChoice)
    application_date = models.DateTimeField("Başvuru tarihi")
    approved = models.BooleanField("Onay durumu", default=False)
    approved_by = models.ForeignKey("profiles.UserProfile", verbose_name="Onaylayan", blank=True, null=True)
    approve_date = models.DateTimeField("Onaylanma tarihi", blank=True, null=True)
    permit_file = models.FileField(upload_to="permit_files", blank=True, null=True)
    need_accommodation = models.BooleanField("Konaklama ihtiyacı", default=0)
    notes = models.TextField("Notlar", blank=True, null=True)

    def __unicode__(self):
        return smart_unicode("{0} - {1}".format(self.user, self.event))

    class Meta:
        db_table = "applications"
        verbose_name = "Başvuru"
        verbose_name_plural = "Başvurular"

