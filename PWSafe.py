# Jay Hayward 2025


# TODO:
# generate output by taking input and xor it by the modifier defined by key
# Create a UI with 2 text boxes from in_str and method
# Accept arguments from text boxes
# Create an executable to make this run-able from any source.

import InParser  # my custom parser script
import base64
from string import printable


def display_info(argv):
    print(f'Printing input string: "{argv.input_str}"')
    print(f'Printing input key: "{argv.key}"')


def create_rule(key):
    str_val = 0
    for i in list(key):
        str_val += ord(i)
    
    rule = str_val % len(printable)

    print(f'rule: +{rule}')
    return(rule)


def generate_ciphertext(plaintext, rule):
    print(f'plaintext: {plaintext}')
    ciphertext = ''
    for i in plaintext:
        j = ((printable.index(i)+rule) % len(printable))
        ciphertext += printable[j]

    # print(f'ciphertext: {ciphertext}')
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
    print(f'ciphetext: {ciphertext}')
    decodedtext = decode_chiphetext(ciphertext, rule)
    print(f'decoded text: {decodedtext}')

    return()



if __name__ == '__main__':
    main()