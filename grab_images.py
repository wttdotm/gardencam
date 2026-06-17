import os
import time
import requests
from datetime import datetime

# Directory to save images
output_dir = "./all_images"
os.makedirs(output_dir, exist_ok=True)

# Camera info
cams = {
    # Existing
    "7x33": "https://webcams.nyctmc.org/api/cameras/1e60ade7-c760-48cf-acd9-d9d6cbfa9420/image",
    "8x31": "https://webcams.nyctmc.org/api/cameras/ec9ffb62-e3bf-4352-8bcf-7c9adf5fbe9c/image?cacheAvoidance=88392",
    "8x33": "https://webcams.nyctmc.org/api/cameras/6a85384f-d82e-4bff-b5f1-15c22cca70e6/image?cacheAvoidance=43456",

    # Central Park
    "5x66": "https://webcams.nyctmc.org/api/cameras/81db80c2-13fe-4ae7-8b47-c08aa42d512f/image",
    "5x60": "https://webcams.nyctmc.org/api/cameras/cd949f21-54b2-4d11-8aae-4ffba8654271/image",
    "6x59": "https://webcams.nyctmc.org/api/cameras/332f161d-47cb-4c8a-b6b6-5ad48a55c978/image",

    # Bryant Park
    "6x42": "https://webcams.nyctmc.org/api/cameras/c34ca47e-e375-4b9f-a8d7-f9737566b783/image",

    # Radio City Music Hall
    "6x50": "https://webcams.nyctmc.org/api/cameras/4f3f56e3-f68e-4b60-a4ba-153ecb9094f7/image",

    # Brooklyn Bowl
    "Wx12": "https://webcams.nyctmc.org/api/cameras/6a5f91d8-042f-4678-a722-2c3c560dedf2/image",

    # Extra Butter (Low Priority)
    "AxD": "https://webcams.nyctmc.org/api/cameras/a249b3ee-bde9-4d6d-9a18-9cd2108d2eb0/image",

    # Le Pistol / Grand Army Plaza
    "GAP1": "https://webcams.nyctmc.org/api/cameras/cb68b8b1-9093-4f2e-acf2-8133b047e8df/image",
    "GAP2": "https://webcams.nyctmc.org/api/cameras/1c51b3ec-3d29-4025-928d-4e182e7c0bd5/image",

    # O'Hanlon's
    "1x14": "https://webcams.nyctmc.org/api/cameras/23994d9e-7e59-4808-8d47-405f779d19cf/image",

    # One4One LES
    "1x1": "https://webcams.nyctmc.org/api/cameras/b5cf34ce-697e-42a1-b22f-8eb2c1f3e79e/image",

    # Delancey & Bowery
    "DxB": "https://webcams.nyctmc.org/api/cameras/a3058350-1552-459f-8379-2fd06895e70a/image",
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