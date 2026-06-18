FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
#CMD ["python", "main1.py"]
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main1:app"]
["gunicorn", "-w", "4", "-k", "gevent", "-b", "0.0.0.0:8080", "--timeout", "120", "main1:app"]