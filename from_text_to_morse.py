import text

shady_text = text.shandy

morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def convert_to_morse(text: str):
    translated = ''
    for letter in text:
        letter = letter.upper()
        if letter != ' ':
            try:
                translated += morse_code_dict[letter] + ' '
            except KeyError:
                translated += ''
        else:
            translated += '  '
    return translated

def main():
    shady_text
    morse_version = convert_to_morse(shady_text)
    print(morse_version)

if __name__ == '__main__':
    main()