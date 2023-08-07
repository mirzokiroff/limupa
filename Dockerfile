FROM python:3.11-alpine

WORKDIR /limupa
COPY . /limupa

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
