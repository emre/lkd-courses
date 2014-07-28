# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User


class Instructor(models.Model):
    fullname = models.CharField("ad soyad", max_length=255)
    avatar = models.ImageField(upload_to="instructor_avatars")

    def __unicode__(self):
        return smart_unicode(self.fullname)

    class Meta:
        db_table = "instructors"
        verbose_name = "Eğitmen"
        verbose_name_plural = "Eğitmenler"


class Sponsor(models.Model):
    name = models.CharField("Sponsor ismi", max_length=255)
    url = models.CharField("Sponsor adres", max_length=255)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        db_table = "sponsors"
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsorlar"


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


SPONSOR_TYPES = (
    ('1', 'platin'),
    ('2', 'altın'),
    ('4', 'gümüş'),
    ('5', 'bronz'),
)


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

class Course(models.Model):
    event = models.ForeignKey(Event)
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
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    course = models.ForeignKey(Course)
    priority = models.IntegerField("Öncelik")  # [1-N]

    def __unicode__(self):
        return smart_unicode("{0} - {1} - {2}".format(self.event, self.course, self.priority))

    class Meta:
        db_table = 'user_choices'
        verbose_name = 'kullanıcı kurs seçimi'
        verbose_name_plural = 'kullanıcı kurs seçimleri'


class Application(models.Model):
    user = models.ForeignKey(User, related_name="application_user")
    course = models.ForeignKey(Event)
    choices = models.ManyToManyField(UserChoice)
    application_date = models.DateTimeField("Başvuru tarihi")
    approved = models.BooleanField("Onay durumu", default=False)
    approved_by = models.ForeignKey(User, verbose_name="Onaylayan", blank=True, null=True)
    approve_date = models.DateTimeField("Onaylanma tarihi", blank=True, null=True)
    permit_file = models.FileField(upload_to="permit_files", blank=True, null=True)
    need_accommodation = models.BooleanField("Konaklama ihtiyacı", default=0)
    notes = models.TextField("Notlar", blank=True, null=True)

    def __unicode__(self):
        return smart_unicode("{0} - {1}".format(self.user, self.course))

    class Meta:
        db_table = "applications"
        verbose_name = "Başvuru"
        verbose_name_plural = "Başvurular"


class AdministrativeNote(models.Model):
    user = models.ForeignKey(User, related_name="notted_user")
    adder = models.ForeignKey(User, related_name="adder")
    note = models.TextField("Not")

    def __unicode__(self):
        return smart_unicode("{0} #{1}".format(self.user, self.id))

    class Meta:
        db_table = "administrative_notes"
        verbose_name = "Yönetimsel not"
        verbose_name_plural = "Yönetimsel notlar"


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField("Adres")
    phone = models.CharField("Telefon numarası", max_length=20)
    company = models.CharField(
        "Çalıştığı şirket",
        blank=True,
        null=True,
        help_text="Kamu çalışanları bağlı oldukları müdürlüğü yazabilir.",
        max_length=255
    )
    public_officer = models.BooleanField("Kamu çalışanı", default=False)
    role = models.CharField("Bağlı olunan departman/bölüm", blank=True, null=True, max_length=255)
    birthdate = models.DateField("Doğum tarihi")
    lkd_id = models.CharField("LKD üye numarası", blank=True, null=True, max_length=32)
    inetd_id = models.CharField("INETD üye numarası", blank=True, null=True, max_length=32)
    github_username = models.CharField("Github kullanıcı adı", max_length=64)

    def __unicode__(self):
        return smart_unicode(self.user.username)

    class Meta:
        db_table = "user_profiles"
        verbose_name = "Kullanıcı profili"
        verbose_name_plural = "Kullanıcı profilleri"