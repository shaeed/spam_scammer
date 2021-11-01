"""Read the data files"""

import pandas as pd
import random
from helper import get_random_string


names_csv = r'../data/names.csv'
passwords_csv = r'../data/passwords.csv'


class Data(object):
    def __init__(self, otp_len: int = 8):
        self.names_df = self.read_csv(names_csv)
        self.name_col = self.names_df.columns[0]
        self.passwords_df = self.read_csv(passwords_csv)
        self.pass_col = self.passwords_df.columns[0]
        # otp
        self.min_otp = int('1' * otp_len)
        self.max_otp = int('9' * otp_len)

    def read_csv(self, file: str) -> pd.DataFrame:
        names = pd.read_csv(file)
        print(f'{file}: {names.describe()}')
        return names

    def get_name(self, truncate: bool = True) -> str:
        name = str(self.names_df[self.name_col].sample().iloc[0])
        if truncate:
            return name[:50]
        return name

    def get_user_id(self) -> str:
        name = self.get_name()
        name = name.replace(' ', '.')
        if len(name) < 8:
            name += '.' + get_random_string(8-len(name))
        return name

    def get_password(self) -> str:
        return self.passwords_df[self.pass_col].sample().iloc[0]

    def get_otp(self) -> str:
        return str(random.randint(self.min_otp, self.max_otp))
