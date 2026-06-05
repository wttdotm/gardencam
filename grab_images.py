import os
import time
import requests
from datetime import datetime

# Directory to save images
output_dir = "./all_images"
os.makedirs(output_dir, exist_ok=True)

# Camera info
cams = {
    "7x33": "https://webcams.nyctmc.org/api/cameras/1e60ade7-c760-48cf-acd9-d9d6cbfa9420/image",
    "8x31": "https://webcams.nyctmc.org/api/cameras/ec9ffb62-e3bf-4352-8bcf-7c9adf5fbe9c/image?cacheAvoidance=88392",
    "8x33": "https://webcams.nyctmc.org/api/cameras/6a85384f-d82e-4bff-b5f1-15c22cca70e6/image?cacheAvoidance=43456"
}

# Grab images every 2 seconds for 1 minute (total 30 times)
duration_sec = 60
interval_sec = 2
iterations = duration_sec // interval_sec

for i in range(iterations):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for cam_name, cam_url in cams.items():
        try:
            resp = requests.get(cam_url, timeout=10)
            if resp.status_code == 200:
                filename = f"{cam_name}_{timestamp}.jpg"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(resp.content)
            else:
                print(f"Failed to get image from {cam_name} ({cam_url}), status: {resp.status_code}")
        except Exception as e:
            print(f"Error fetching {cam_name}: {e}")
    if i < iterations - 1:
        time.sleep(interval_sec)