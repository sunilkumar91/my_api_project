import requests
import time

URL = "https://www.google.com"
INTERVAL = 10  # సెకన్లలో గ్యాప్

def monitor_website():
    print(f"Monitoring started for: {URL}...")
    
    try:
        while True:  
            response = requests.get(URL)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
        if response.status_code == 200:
            print(f"[{timestamp}] Success! Status Code: {response.status_code}", flush=True) 
        else:
            print(f"[{timestamp}] Alert! Status Code: {response.status_code}", flush=True)
                
            time.sleep(INTERVAL) 
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    monitor_website()