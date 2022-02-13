FROM python:3.10.2-alpine AS meteorologist

COPY . /var/www/meteorologist

WORKDIR /var/www/meteorologist
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w 4", "app:app", "--threads 2", "-b 0.0.0.0:8000"]