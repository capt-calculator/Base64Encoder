#!/usr/bin/python3

from math import ceil
import base64


class Base64e:

    def __init__(self):
        self.base64_encoding = {
            '000000': 'A',	'010000': 'Q',	'100000': 'g',	'110000': 'w',
            '000001': 'B',	'010001': 'R',	'100001': 'h',	'110001': 'x',
            '000010': 'C',	'010010': 'S',	'100010': 'i',	'110010': 'y',
            '000011': 'D',	'010011': 'T',	'100011': 'j',	'110011': 'z',
            '000100': 'E',	'010100': 'U',	'100100': 'k',	'110100': '0',
            '000101': 'F',	'010101': 'V',	'100101': 'l',	'110101': '1',
            '000110': 'G',	'010110': 'W',	'100110': 'm',	'110110': '2',
            '000111': 'H',	'010111': 'X',	'100111': 'n',	'110111': '3',
            '001000': 'I',	'011000': 'Y',	'101000': 'o',	'111000': '4',
            '001001': 'J',	'011001': 'Z',	'101001': 'p',	'111001': '5',
            '001010': 'K',	'011010': 'a',	'101010': 'q',	'111010': '6',
            '001011': 'L',	'011011': 'b',	'101011': 'r',	'111011': '7',
            '001100': 'M',	'011100': 'c',	'101100': 's',	'111100': '8',
            '001101': 'N',	'011101': 'd',	'101101': 't',	'111101': '9',
            '001110': 'O',	'011110': 'e',	'101110': 'u',	'111110': '+',
            '001111': 'P',	'011111': 'f',	'101111': 'v',	'111111': '/'
        }


    def encode(self, input):

        # convert ASCII characters to binary representation
        octets = [format(ord(c), '08b') for c in input]

        # combine octets into single binary string
        binary = ''.join(octets)

        # determine number of sextets needed 
        n_sextets = ceil(len(binary) / 6)

        # determine # of zeroes for padding
        remainder = 6 * n_sextets - len(binary)

        # append zeroes to binary string
        binary = binary + ('0' * remainder)

        # split binary string into 6-bit sextets
        sextets = [binary[i:i+6] for i in range(0, len(binary), 6)]

        # convert 6-bit sextets to Base64 encoding, add '=' padding
        output = ''.join([self.base64_encoding[b] for b in sextets]) + "=" * (remainder // 2)

        return output 


    def decode(self, input):

        # determine padding
        padding = input.count('=')

        # remove padding
        input = input.replace("=", "")
        
        # convert characters to binary sextets using Base64 table
        binary = [key for char in input for key, value in self.base64_encoding.items() if char == value]

        # join sextets into single binary string
        binary = ''.join(binary)

        # remove number of trailing zeroes as determined by padding
        binary = binary[:-(padding*2)] if padding else binary

        # split binary string into 8-bit binary octets
        octets = [binary[i:i+8] for i in range(0, len(binary), 8)]

        # convert octets back to ASCII characters
        output = [chr(int(octet, 2)) for octet in octets]

        # combine ASCII characters to string
        output = ''.join(output)
        
        return output


if __name__ == "__main__":
    input = input("Enter text to encode: ")
    encoder = Base64e()
    encoded = encoder.encode(input)
    decoded = encoder.decode(encoded)

    module_encoded = base64.b64encode(input.encode()).decode('utf-8')
    module_decoded = base64.b64decode(module_encoded).decode()

    print("Encoded values: ", f"Our encoder:           {encoded}", f"base64 module encoder: {module_encoded}", sep="\n")
    print("Decoded values: ", f"Our decoder:           {decoded}", f"base64 module decoder: {module_decoded}", sep="\n")

