import time
import httpx
from datetime import datetime

SERVER_URL = "http://127.0.0.1:8000"
DEVICE_ID = "demo-device-001"

def send_heartbeat():
    payload = {
        "device_id": DEVICE_ID,
        "status": "online",
        "policy_version": 1
    }
    try:
        response = httpx.post(f"{SERVER_URL}/heartbeat", json=payload, timeout=5.0)
        print(f"[{datetime.now()}] Heartbeat sent: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"[{datetime.now()}] Failed to send heartbeat: {e}")

if __name__ == "__main__":
    print(f"Starting OpenGuard Kids Agent (Week 1 minimal)...")
    print(f"Device ID: {DEVICE_ID}")
    print(f"Server URL: {SERVER_URL}")
    print(f"Heartbeat interval: 60 seconds")
    
    # Send immediately on startup, then every 60s
    send_heartbeat()
    
    while True:
        time.sleep(60)
        send_heartbeat()
