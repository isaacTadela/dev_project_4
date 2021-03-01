FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN chmod 644 rest_app.py
CMD ["python", "-u", "rest_app.py"]
EXPOSE 5000
