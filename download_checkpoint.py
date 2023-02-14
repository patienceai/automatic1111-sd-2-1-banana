import os
import requests
import sys
import time
from tqdm import tqdm

MODEL_URL = os.environ.get('MODEL_URL')
HF_TOKEN = os.environ.get('HF_TOKEN', '')

CHUNK_SIZE = 1024 * 1024

def get_filename(MODEL_URL):
    if '.safetensors' in MODEL_URL:
        return 'models/Stable-diffusion/model.safetensors'
    else:
        return 'models/Stable-diffusion/model.ckpt'

def check_model_file(filename):
    file_size_mb = round(os.path.getsize(filename) / (1024 * 1024))
    if file_size_mb < 100:
        print(f'The downloaded file is only {file_size_mb} MB and does not appear to be a valid model.')
        sys.exit(1)

def download_hf_file(MODEL_URL, HF_TOKEN):
    filename = get_filename(MODEL_URL)
    print("Model URL:", MODEL_URL)
    print("Download Location:", filename)
    if not HF_TOKEN:
        print("A Huggingface token was not provided.")
    else:
        print("Using Huggingface authentication token.")
    time.sleep(1)
    headers = {'Authorization': f'Bearer {HF_TOKEN}'}
    response = requests.get(MODEL_URL, headers=headers, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as f, tqdm(desc="Downloading", unit="bytes", total=int(response.headers.get('content-length', 0))) as progress:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
                progress.update(len(chunk))
    check_model_file(filename)

def download_other_file(MODEL_URL):
    filename = get_filename(MODEL_URL)
    print("Model URL:", MODEL_URL)
    print("Download Location:", filename)
    time.sleep(1)
    response = requests.get(MODEL_URL, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as f, tqdm(desc="Downloading", unit="bytes", total=int(response.headers.get('content-length', 0))) as progress:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
                progress.update(len(chunk))
    check_model_file(filename)

if 'huggingface.co' in MODEL_URL:
    if '/blob/' in MODEL_URL:
        MODEL_URL = MODEL_URL.replace('/blob/', '/resolve/')
    download_hf_file(MODEL_URL, HF_TOKEN)
else:
    download_other_file(MODEL_URL)
