# Jay Hayward 2025

# TODO:
# Convert algorithm to b64 encoding (method % 64)

# Create a UI with 2 text boxes from in_str and method
# Accept arguments from text boxes
# Create an executable to make this run-able from any source.

import InParser  # my custom parser script

def main():
    argv = InParser.CustomParser()
    print(f'Printing input string: "{argv.input_str}"')

    if(argv.alg == 'base64'):
        # do stuff
        return()



if __name__ == '__main__':
    main()