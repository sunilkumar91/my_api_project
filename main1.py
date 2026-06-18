from flask import Flask
import requests
import time
import threading
import os

app = Flask(__name__)

# 1. మానిటర్ చేయాల్సిన వెబ్‌సైట్ల లిస్ట్
WEBSITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org"
]

results = {url: "Checking..." for url in WEBSITES}

# 2. వెబ్‌సైట్ మానిటరింగ్ ఫంక్షన్
def monitor_websites():
    while True:
        for url in WEBSITES:
            try:
                response = requests.get(url, timeout=5)
                results[url] = f"Status Code: {response.status_code}"
            except Exception as e:
                results[url] = f"Error: {str(e)}"
        time.sleep(20)

# మానిటరింగ్ థ్రెడ్ ఇక్కడ గ్లోబల్ స్కోప్‌లో ఉంది, కాబట్టి Gunicorn దీన్ని రన్ చేస్తుంది
if 'gunicorn' in os.environ.get('SERVER_SOFTWARE', ''):
    if not hasattr(app, 'thread_started'):
        threading.Thread(target=monitor_websites, daemon=True).start()
        app.thread_started = True
else:
    # లోకల్‌గా రన్ చేసేటప్పుడు థ్రెడ్ స్టార్ట్ అవ్వడానికి
    threading.Thread(target=monitor_websites, daemon=True).start()

# 3. వెబ్ పేజీ డాష్‌బోర్డ్
@app.route('/')
def home():
    styles = """
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
        table { border-collapse: collapse; width: 100%; background-color: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        th, td { padding: 15px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #2c3e50; color: white; }
        .refresh-btn { 
            padding: 12px 25px; background-color: #3498db; color: white; 
            border: none; cursor: pointer; border-radius: 5px; font-size: 16px;
        }
    </style>
    """
    html = f"<html><head>{styles}</head><body>"
    html += "<h1>Website Monitor Dashboard</h1>"
    html += '<button class="refresh-btn" onclick="location.reload()">Refresh Data</button><br><br>'
    html += "<table><tr><th>URL</th><th>Status</th></tr>"
    for url, status in results.items():
        html += f"<tr><td>{url}</td><td>{status}</td></tr>"
    html += "</table></body></html>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)