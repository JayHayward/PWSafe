# Jay Hayward 2025


# TODO:
# generate output by taking input and xor it by the modifier defined by key
# Create a UI with 2 text boxes from in_str and method
# Accept arguments from text boxes
# Create an executable to make this run-able from any source.

import InParser  # my custom parser script


def display_info(argv):
    print(f'Printing input string: "{argv.input_str}"')
    print(f'Printing input string: "{argv.key}"')


def create_rule(key):
    str_val = 0
    ascii_offset = 32
    for i in list(key):
        str_val += ord(i) - ascii_offset

    modifier = str_val % 95

    return(modifier)


def generate_output(input_str, rule):
    # tmp
    out_str = input_str

    return(out_str)


def main():
    argv = InParser.CustomParser()
    # display_info(argv)
    rule = create_rule(argv.key)
    output = generate_output(argv.input_str, rule)
    print(output)

    return()



if __name__ == '__main__':
    main()