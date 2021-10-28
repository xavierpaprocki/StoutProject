import pandas as pd
import csv


def main():
    location = 'C:\\Users\\papro\\PycharmProjects\\StoutProject\\data\\loans_full_schema.csv'
    data = pd.read_csv(location)
    print('here')
    print(data)
    print('here')
    return data


if __name__ == 'main':
    main()
