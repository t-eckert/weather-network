FROM python:3.10.2-alpine AS reporter

COPY . /var/www/reporter

WORKDIR /var/www/reporter
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w 4", "app:app", "--threads 2", "-b 0.0.0.0:8000"]