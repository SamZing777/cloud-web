FROM python:3.10.4

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
