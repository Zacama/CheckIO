MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    message = code.split(" ")
    result = ""
    add_space = False
    for x in message:
        if x == '':
            if add_space is False:
                result += " "
                add_space = True
        else:
            result += MORSE[x]
            add_space = False
    if result[0].isalpha():
        letter = result[0].capitalize()
        result = letter + result[1:]
    return result


if __name__ == '__main__':
    print(morse_decoder("... --- -- .   - . -..- -"))
