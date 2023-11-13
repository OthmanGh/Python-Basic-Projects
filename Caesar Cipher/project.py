#*Caeser Cipher
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs 

    #TODO-2: inside the 'encrypt' function, shift each letter of the 'text' forwoards in the alphabet by the shift amount and print the encrypted text
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqql"

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message
#TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print hte decrypted text.
    #e.g.
    #cipherr_tet = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

#TODO-6:  Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test teh code to encryptp *AND* decrypt a message

# #* Todos : 1 - 2 - 3 : 
# def encrypt(text, shift):
#     encoded_message = []
#     for letter in text:
#         encoded_indx = alphabet.index(letter)
#         encoded_message.append(alphabet[encoded_indx + int(shift)])
#     encoded_message = ''.join(encoded_message)
#     print(f"The encoded text is {encoded_message}")

#  #* Todos :  4 - 5 - 6
# def decrypt(text, shift):
#     decrypt_message =""
#     for char in text:
#         decrypt_idx = alphabet.index(char)
#         decrypt_char = alphabet[decrypt_idx - shift]
#         decrypt_message += decrypt_char
#     print(f"The decoded text is {decrypt_message}")

# if direction == 'encode':
#     encrypt(text= text, shift= shift)
# elif direction == 'decode':
#     decrypt(text = text, shift = shift)
# else:
#     print("You've entered unvalid data")

# from art import logo


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(starter_text, shift_val, direction_val):
#     end_text = []
#     if direction_val == 'decode':
#         shift_val *= -1
#     for char in starter_text:
#         char_idx = alphabet.index(char)
#         char_conversion = alphabet[char_idx + shift_val]
#         end_text.append(char_conversion)
#     print(f"The {direction_val} text is {''.join(end_text)}")


# caesar(starter_text= text, shift_val= shift, direction_val = direction)



#TODO-7: Import and print the logo from art.py when the program starts.
#TODO-8: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
#TODO-9: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
#TODO-10: Can you figure out a way to ask the user if they want to restart the cipher program?
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

from art import logo

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True

print(logo)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")






