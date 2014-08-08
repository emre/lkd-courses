# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from courses.models import Instructor

INSTRUCTOR_LIST = [
    'Adil İlhan',
    'Ahmet Sınak',
    'Ahmet Sınak',
    'Aydın T. Doyak',
    'Ahmet Sınak',
    'Çağdaş Direk',
    'Ahmet Sınak',
    'D. Destan Sarpkaya',
    'Ahmet Sınak',
    'Emre Eryılmaz',
    'Ahmet Sınak',
    'Eray Aslan',
    'Ahmet Sınak',
    'Fatih Erikli',
    'Ahmet Sınak',
    'Hakan Uygun',
    'Ahmet Sınak',
    'Hidayet Doğan',
    'Ahmet Sınak',
    'Levent Emmungil',
    'Ahmet Sınak',
    'H. Murat Yıldırım',
    'Ahmet Sınak',
    'Onur R. Bingöl',
    'Ahmet Sınak',
    'Ömer Özkan',
    'Ahmet Sınak',
    'Samed Beyribey',
    'Ahmet Sınak',
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

        print "shields up, weapons online."