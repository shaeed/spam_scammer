from read_data import Data
from helper import send_data


def gen_1(data: Data) -> dict:
    return {"username": data.get_user_id(), "password": data.get_password()}


def gen_2(data: Data) -> dict:
    return {'otp': data.get_otp()}


# base domain url, like http://ekycupdatenow.in
base_url = r'http://ekycupdatenow.in'
# all the forms url and corresponding fun to generate the data
forms_ulr = [(r"1.php", gen_1),
             (r"2.php", gen_2),
             (r"4.php", gen_2),
             (r"5.php", gen_2),
             (r"6.php", gen_2),
             (r"7.php", gen_2),
             (r"3.php", gen_2)]


def main():
    data = Data(otp_len=8)
    for i in range(10000):
        for url, generator in forms_ulr:
            ulr = f'{base_url}/{url}'
            form_data = generator(data)
            print(i, ulr, form_data)
            # send_data(form_data, url)


if __name__ == '__main__':
    main()
