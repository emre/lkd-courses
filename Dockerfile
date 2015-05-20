FROM python:2.7
RUN mkdir /lyk2015
ADD ./requirements.txt /lyk2015/
WORKDIR /lyk2015
RUN pip install -r requirements.txt
ADD ./lkdcourses /lyk2015/
EXPOSE 8000
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
