# -*- coding: utf-8 -*-

from __future__ import print_function

from django.core.management.base import BaseCommand, CommandError

from courses.models import Instructor

INSTRUCTOR_LIST = [
    'Adil İlhan',
    'Ahmet Sınak',
    'Ali Burak Öncül',
    'Aydın T. Doyak',
    'Barkın Kılıç',
    'Çağdaş Direk',
    'Çağrı Ersen',
    'D. Destan Sarpkaya',
    'Doruk Fişek',
    'Emre Eryılmaz',
    'R. Engür Pişirici',
    'Eray Aslan',
    'Erdem Bayer',
    'Fatih Erikli',
    'Fatih N. Yarcı',
    'Hakan Uygun',
    'Halit Alptekin',
    'Hidayet Doğan',
    'H. Kemal Taşkın',
    'Levent Emmungil',
    'Mehmet Dursun İnce',
    'H. Murat Yıldırım',
    'Mustafa Akgül',
    'Onur R. Bingöl',
    'Osman Ünalan',
    'Ömer Özkan',
    'Osman Ünalan',
    'Samed Beyribey',
    'Süleyman Özarslan',
    'Tayfun Öziş Erikan',
]


class Command(BaseCommand):
    help = 'Imports initial instructors'

    def handle(self, *args, **options):
        for instructor_name in INSTRUCTOR_LIST:
            try:
                instructor = Instructor.objects.get(fullname=instructor_name)
            except Instructor.DoesNotExist:
                instructor = Instructor(fullname=instructor_name)
                instructor.save()

        print("shields up, weapons online.")
