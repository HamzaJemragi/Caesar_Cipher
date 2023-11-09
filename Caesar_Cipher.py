import Caesar_art
def caeser(text,shift,direction):
    if direction != 'encode' and direction != 'decode':
        print('Wrong direction!!')
        return 
    t = []
    l = []
    for char in text:
        t.append(char)
    for char in t:
        if char not in alphabet:
            l.append(char)
        for letter in alphabet:
            if char == letter:
                indice = alphabet.index(letter)
                if direction == 'encode':
                    indice += shift
                    while indice > 25:
                        indice -= 26
                elif direction == 'decode':
                    indice -= shift
                    while indice < 0:
                        indice += 26
                l.extend(alphabet[indice])
    t.clear()
    t.extend(l)
    new_text = ""
    for char in t:
        new_text += char
    print(f'The {direction}d text is : {new_text}')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(Caesar_art.logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice != 'yes':
        print('Goodbye')
        break