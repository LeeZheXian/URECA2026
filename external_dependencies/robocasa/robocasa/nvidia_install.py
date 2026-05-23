import urllib.request
import os

local_dir = "/home/zijun/zxp/Isaac-GR00T-N1.5/external_dependencies/robocasa/robocasa/models/assets/objects/usd_ver"
os.makedirs(local_dir, exist_ok=True)

# These are the current verified paths for Isaac Sim 4.x assets
assets = {
    "pen.usd": "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.0/Isaac/Props/Office/pencil.usd",
    "marker.usd": "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.0/Isaac/Props/Office/marker_blue.usd",
    "tape_roll.usd": "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.0/Isaac/Props/Office/tape_masking.usd"
}

def download_asset(name, url):
    save_path = os.path.join(local_dir, name)
    print(f"Attempting download: {name}...")
    try:
        # Adding a User-Agent header sometimes helps with S3 bucket permissions
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as response:
            with open(save_path, 'wb') as f:
                f.write(response.read())
        print(f"✅ Success: {save_path}")
    except Exception as e:
        print(f"❌ Failed {name}: {e}")

for name, url in assets.items():
    download_asset(name, url)