morse_code = {
    # Letters
    "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",   "e": ".",
    "f": "..-.",  "g": "--.",   "h": "....",  "i": "..",    "j": ".---",
    "k": "-.-",   "l": ".-..",  "m": "--",    "n": "-.",    "o": "---",
    "p": ".--.",  "q": "--.-",  "r": ".-.",   "s": "...",   "t": "-",
    "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",  "y": "-.--",
    "z": "--..",

    # Digits
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    # Punctuation and special characters
    ".": ".-.-.-",    ",": "--..--",    "?": "..--..",    "'": ".----.",
    "!": "-.-.--",    "/": "-..-.",     "(": "-.--.",     ")": "-.--.-",
    "&": ".-...",     ":": "---...",    ";": "-.-.-.",    "=": "-...-",
    "+": ".-.-.",     "-": "-....-",    "_": "..--.-",    '"': ".-..-.",
    "$": "...-..-",   "@": ".--.-.",    "¿": "..-.-",     "¡": "--...-",

    # Space between words
    " ": "   "
}


def convert_text(message):
    converted_text = ""
    message_list = list(message)
    for letter in message_list:
        converted_text += f"{morse_code[letter]} "
    print(f"Converted text: {converted_text}")


def convert_morse_code(message):
    words = message.strip().split("   ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        for code in letters:
            found = [k for k, v in morse_code.items() if v == code]
            if found:
                decoded_letters.append(found[0])
            else:
                decoded_letters.append('?')
        decoded_words.append("".join(decoded_letters))
    converted_morse = " ".join(decoded_words)
    print(f"Converted Morse: {converted_morse}")


go_again = "yes"
while go_again == "yes":
    create_read = input("If you want to convert a message to Morse Code type 'create', if you want to read Morse code type 'read': ")
    if create_read == "create":
        text = input("Please type your message: ").lower()
        convert_text(text)

    elif create_read == "read":
        morse = input("Please enter the Morse Code: ").lower()
        convert_morse_code(morse)

    else:
        print("Please choose a valid option.")

    go_again = input("Do you want to read or create more Morse Code? (yes, no): ")
    if go_again != "yes" or go_again != "no":
        go_again = input("Please choose a valid option. Do you want to read or create more Morse Code? (yes, no): ")
