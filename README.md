lkd-courses
===========

LKD bunyesinde gerceklestirilen kurslar icin yonetim yazilimi.

## Kurulum

```sh
$ python3.4 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ cd lkdcourses/
$ cp base/local_settings.dist base/local_settings.py
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
