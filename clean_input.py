import re


def clean_input(input):
    data = input
    data.replace(',', '.')
    decimal_string = re.findall('\d*\.?\d+', data)
    if decimal_string:
        return decimal_string[0]

    decimal_string = re.findall('\.\d+', data)
    if decimal_string:
        return '0' + decimal_string[0]
