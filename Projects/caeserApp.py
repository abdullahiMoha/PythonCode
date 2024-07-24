""" 
This little project allows you to encode and decode 
words by using speciall method called 'Ceaser Cipher'

Feel free to use by your own words
"""
from Arts.caeser_art import logo
# Write your code below this line 👇

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# impoerting the system logo
print(logo)


def caeser(dire, p_text, shift_n):
    """Encrypting adn Decrytiong text"""

    plain_text = ""
    # checking what the user want to do 'encode' or 'decode'
    if dire == "decode":
        shift_n *= -1

    for let in p_text:
        if let in alphabet:
            index = alphabet.index(let)
            plain_text += alphabet[index+shift_n]
        else:
            plain_text += let

    print(f"here is {dire}d result: {plain_text}")


again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    # Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caeser(dire=direction, p_text=text, shift_n=shift)

    # Asking if the user want to try again the game
    option = input("if you want again 'yes' otherwise 'no'").lower()
    if option == "no":
        # os.system("cls")
        again = False
        print("Hav nice day")
