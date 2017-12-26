FROM python:3.6-slim
WORKDIR /ics_project
ADD . /ics_project

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
