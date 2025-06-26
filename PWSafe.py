# Jay Hayward 2025

# TODO:
# Create a UI with 2 text boxes from in_str and method
# Accept arguments from text boxes
# Create an executable to make this run-able from any source.

import InParser  # my custom parser script


def display_info(argv):
    print(f'Printing input string: "{argv.input_str}"')
    print(f'Printing input string: "{argv.key}"')

    if(argv.key == 'base64'):
        # do stuff
        return()

def create_rule(key):
    # Bse64 elphabet: [A-Za-z0-9+/=]
    str_val = 0
    for i in list(key):
        str_val += ord(i)

    modifier = str_val % 64

    # print(f'key value: {str_val}')
    # print(f'modifier: {modifier}')

    return(modifier)

def encdode_input(input_str, rule):
    out_str = ''
    for i in input_str:
        j = chr(ord(i) + rule)
        out_str += j

    return(out_str)


def main():
    argv = InParser.CustomParser()
    # display_info(argv)
    rule = create_rule(argv.key)
    output = encdode_input(argv.input_str, rule)
    print(output)

    return()



if __name__ == '__main__':
    main()