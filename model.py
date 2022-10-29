from encodings import utf_8
import csv


def read_txt():
    with open('Phonebook1.txt', 'r', encoding='utf_8') as f1:
        print(f1.read())


def read_csv():
    with open('Phonebook2.csv', encoding='utf-8') as f:
       f_reader = csv.reader(f, delimiter = ',')
       for row in f_reader:
        print(f'{" ".join(row)}')

          
       

def write_txt(info):
    with open('Phonebook1.txt','a', encoding='utf-8') as data:
        data.write(
            f'\nФамилия: {info[0]}\nИмя: {info[1]}\nТел: {info[2]}\nОписание: {info[3]}')


def write_csv(info):
    with open('Phonebook2.csv','a', encoding='utf-8') as f:
        f_writer = csv.writer(f, delimiter=",",lineterminator="\r")
        f_writer.writerow(info)
