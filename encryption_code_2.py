import random
import string
import pyperclip

ed = input("Do you want to encrypt or decrypt the message [e/d]?\n")

letter_list = list(string.ascii_letters + string.digits + string.punctuation + " ")
shuffle_list = letter_list.copy() #creating a copy of the list not using the actual list

def inputs():
    message = input("Please input your message:\n")
    number = int(input("Input the seed:\n"))
    return message, number

def ed_code(ed=ed, letter_list=letter_list, shuffle_list=shuffle_list): #default parameters e.g. ed=ed
    message, number = inputs()
    random.Random(number).shuffle(shuffle_list)

    print(shuffle_list)

    if ed.lower() == "e":
        encode_dict = dict(zip(letter_list, shuffle_list)) #dict(zip(key,value))

        print(encode_dict)

    else:
        encode_dict = dict(zip(shuffle_list, letter_list))

    print(shuffle_list)

    final_message = ""
    for i in message:
        final_message += encode_dict[i]

    return final_message

final_message = ed_code()  # after using default parameters when you call the function no need to put these parameters in
pyperclip.copy(final_message) #allows you to paste the e/d code without copying it
print(f"Your message is: \n{final_message}")

# def ed_code(letter_list, shuffle_list):
#     if ed.lower() == "e": #turns uppercase to lowercase and if input a lowercase letter it remains the same
#         message, number = inputs()
#
#         random.Random(number).shuffle(shuffle_list)
#         encrypt_dict = dict(zip(letter_list, shuffle_list))
#
#         encrypt_list = []
#         for i in message:
#             encrypt_list.append(encrypt_dict[i])
#
#         encrypt_message = "".join(encrypt_list)
#         pyperclip.copy(encrypt_message)
#         print(encrypt_message)
#
#     else:
#         message, number = inputs()
#
#         random.Random(number).shuffle(shuffle_list)
#         decrypt_dict = dict(zip(shuffle_list, letter_list,))
#
#         decrypt_list = []
#         for i in message:
#             decrypt_list.append(decrypt_dict[i])
#
#         decrypt_message = "".join(decrypt_list)
#         print(decrypt_message)

# ed_code(ed, letter_list, shuffle_list) before using default parameters when you called the function needed to put these parameters in
