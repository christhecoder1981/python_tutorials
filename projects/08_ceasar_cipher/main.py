alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift_number):
    encoded_result = ""
    for letter in message: # as
        if letter in alphabet:
            index_no = alphabet.index(letter) + shift_number # 2
            encoded_result += alphabet[index_no]
        else:
            encoded_result += letter
    print(f"Here's the encoded result: {encoded_result}")
def decode(message, shift_number):
    decoded_result = ""
    for letter in message: # as
        if letter in alphabet:
            index_no = alphabet.index(letter) - shift_number # 2
            decoded_result += alphabet[index_no]
        else:
            decoded_result += letter
    print(f"Here's the decoded result: {decoded_result}")

while True:
    choose = input("Type encode to encrypt, type decode to decrypt: ")
    mess = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if choose == "encode":
        encode(mess, shift)
    elif choose == "decode":
        decode(mess, shift)

    again = input("Do you want to go again, type yes. Otherwise type no. ")
    if again == "yes":
        continue
    elif again == "no":
        break