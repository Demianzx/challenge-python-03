import os
import sys
import re


def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        mensaje = re.findall("[a-z]",text)
        print(mensaje)



if __name__ == '__main__':
    run()
