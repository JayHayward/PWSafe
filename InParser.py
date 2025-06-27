# Jay Hayward 2025



from argparse import ArgumentParser
import base64

def CustomParser():
    # Read and parse arguments
    parser = ArgumentParser(description="takes a string and encodes it using an encoding algorithm")
    parser.add_argument('input_str', 
                        help = "The string to encode", 
                        type = str)
    parser.add_argument('--key', 
                        help = "The encoding algorithm to use", 
                        type = str, 
                        default = 'base64')
    argv = parser.parse_args()
    return(argv)



if __name__ == '__main__':
    RuntimeError('DO NOT RUN THIS FILE DIRECTLY')
