FROM python:3.9-slim
WORKDIR /app
# మొదట requirements.txt ని కాపీ చేయండి
COPY requirements.txt .
# ఆ తర్వాత ప్యాకేజీలను ఇన్‌స్టాల్ చేయండి
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#CMD ["python", "main1.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main1:app"]