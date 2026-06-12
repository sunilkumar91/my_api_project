from flask import Flask
import requests
import time
import threading

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

# 3. వెబ్ పేజీ డాష్‌బోర్డ్ (CSS మరియు HTML తో)
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
            transition: background 0.3s;
        }
        .refresh-btn:hover { background-color: #2980b9; }
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

# 4. ఫైల్‌లోని కోడ్‌ను లైన్-బై-లైన్ ప్రింట్ చేసే ఫంక్షన్ (మీరు అడిగినట్లుగా)
def print_file_lines():
    with open('main1.py', 'r') as file:
        lines = file.readlines()
        print("\n--- Code lines in main1.py ---")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")

if __name__ == "__main__":
    # మానిటరింగ్ స్టార్ట్ చేయండి
    threading.Thread(target=monitor_websites, daemon=True).start()
    
    # ఫైల్ లైన్స్ ప్రింట్ చేయండి
    print_file_lines()
    
    # సర్వర్ స్టార్ట్ చేయండి
    app.run(host='0.0.0.0', port=8080)
