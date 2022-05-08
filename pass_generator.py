#!/usr/bin/env python3

import argparse, random, string

def get_arguments():
    parser = argparse.ArgumentParser(prog="pass_generator", formatter_class=argparse.RawTextHelpFormatter, description='''Generates a badass password for u

Examples:
    python3 pass_generator.py
    python3 pass_generator.py -l 12 -p 'foo@@@N++#'
    python3 pass_generator.py --pattern 'john/@5++
    python3 pass_generator.py -p '!###/@@@+++' --output '/home/user/pass.txt'
    python3 pass_generator.py --pattern '!&&&@#/#5' --length 32 --exclude 'a b c d' -o 'passwords.txt' 'w'
''')

    parser.add_argument('-l', '--length', nargs=1, type=int, default=8,
                        help='Self-explainable. It defines how long the generated password should be. Default is 8.')
    parser.add_argument('-p', '--pattern', help="Defines a pattern for the password, if it is longer than the defined length, overrides it. If not, program will autocomplete remaining with random characters. \n'@' - Any character \n'#' - Letters\n'!' - Uppercase letters\n'&' - Lowercase letters\n'$' - Special characters\n'+' - Numbers\n'/' - Use to override pattern characters\n   e.g: '/@' wouldn't return a random character, but '@' itself  ")
    parser.add_argument('-e', '--exclude', nargs=1,
                        help="Exclude user-defined characters, must be passed in single string separated by spaces.\n   e.g: 'a b c'")
    parser.add_argument('-o', '--output', nargs='+',
                        help="First arg is for path and it's required, second is optional for write mode, default is (a)ppend, you can also use (w)rite.")

    arguments = parser.parse_args()
    return arguments


def generate(length, pattern, output, exclude):
    output = ''
    char = ''

    if type(length) == list:
        length = int(length[0])

    if pattern:
        i = 0
        jump_next_char = False
        for character in pattern:
            if character != "/":
                if jump_next_char == True:
                    jump_next_char = False
                elif character == "@":
                    output += str(chr(random.randrange(33, 126)))
                elif character == "#":
                    output += random.choice(string.ascii_letters)
                elif character == "!":
                    output += random.choice(string.ascii_uppercase)
                elif character == "&":
                    output += random.choice(string.ascii_lowercase)
                elif character == "$":
                    output += random.choice(string.punctuation)
                elif character == "+":
                    output += random.choice(string.digits)
                else:
                    output += character
            else:
                position = pattern.index(character, i)
                output += pattern[position + 1]
                jump_next_char = True
            i += 1
        length -= len(output)

    for i in range(length):
        char = str(chr(random.randrange(33, 126)))
        output += char

    if exclude:
        exclude = ''.join(exclude)
        exclude = exclude.split(' ')
        for character in exclude:
            char = random.choice(str(chr(random.randrange(33, 126))))
            if character in output:
                while char in exclude:
                    char = random.choice(str(chr(random.randrange(33, 126))))
                output = output.replace(character, char)

    print(output)
    return output


args = get_arguments()
output = generate(args.length, args.pattern, args.output, args.exclude)

if args.output:
    try:
        if len(args.output) < 2:
            mode = 'a'
        else:
            mode = args.output[1]
        with open(args.output[0], mode) as file:
            file.write(f'{output}\n')

    except IsADirectoryError:
        print("\n> Couldn't save the file! Make sure you provided the right location. Ex.:'/home/john/test.txt'")
    except ValueError:
        print("\n> Couldn't save the file! Wrong value set for operation mode, choose (w)rite or (a)ppend.")
    except PermissionError:
        print("\n> Couldn't save the file! It seems you don't have permission to do so.")
    except:
        print("\n> Something went wrong, but I'm not sure what!")
