
import string
import random
import requests
import time


def get_random_string(length=10) -> str:
    # choose from all lowercase letter
    # letters = string.ascii_letters + string.digits
    letters = string.printable
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def generate_mobile_no() -> int:
    return random.randint(7123456789, 9123456789)


def generate_otp(length: int = 8):
    min_no = int('1' * length)
    max_no = int('9' * length)
    return random.randint(min_no, max_no)


def send_data(data, url):
    try:
        # res = requests.post("https://8afc-2409-4064-489-9996-69ba-68a7-6bb6-3135.ngrok.io/1.php", data=data)
        res = requests.post(url, data=data, verify=False)
        print(res.text[:100])
    except Exception as e:
        print(e)
        sleep_time = random.randint(5, 60)
        print(f'sleeping for {sleep_time}')
        time.sleep(sleep_time)
