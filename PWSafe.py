# Jay Hayward 2025


# TODO:
# Create a UI with 2 text boxes from input_string and key
# Accept arguments from text boxes
# Create an executable to make this run-able from any source.

import InParser  # my custom parser script
import base64
from string import printable


def display_info(argv):
    print(f'Print input string: "{argv.input_str}"')
    print(f'Print input key: "{argv.key}"')


def create_rule(key):
    str_val = 0
    for i in list(key):
        str_val += ord(i)  # total ascii value of all data in string
    
    rule = str_val % len(printable)  # restrict the rule to keep affected text in printable range

    print(f'rule: +{rule}')
    return(rule)


def generate_ciphertext(plaintext, rule):
    print(f'plaintext: {plaintext}')
    ciphertext = ''
    for i in plaintext:
        j = ((printable.index(i)+rule) % len(printable))  # for ever character in plaintext, keep it within printable range
        ciphertext += printable[j]

    return(ciphertext)


def decode_chiphetext(ciphertext, rule):
    decoded_text = ''
    for i in ciphertext:
        j = ((printable.index(i)-rule) % len(printable))
        decoded_text += printable[j]

    return(decoded_text)


def main():
    argv = InParser.CustomParser()
    # display_info(argv)
    rule = create_rule(argv.key)  # how to modify the plaintext into ciphertext
    ciphertext = generate_ciphertext(argv.input_str, rule)
    print(f'ciphertext: {ciphertext}')
    decodedtext = decode_chiphetext(ciphertext, rule)
    print(f'decoded text: {decodedtext}')

    return()



if __name__ == '__main__':
    main()