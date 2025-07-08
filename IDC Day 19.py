import requests
from concurrent.futures import ThreadPoolExecutor

# List of URLs to download
urls = [
    "https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg",
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
]
# Function for downloading our image files from a URL
def download_file(url):
    local_filename = url.split("/")[-1]
    print(f"Downloading {local_filename}...")
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"{local_filename} downloaded.")
    return local_filename

# Use ThreadPoolExecutor to download concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_file, urls)
