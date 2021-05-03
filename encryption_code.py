import random

ed = input("Do you want to encrypt or decrypt the message [e/d]?\n")
number = input("Input the seed:\n") #always put inouts together at the top of the code

def messages(): # always return with a function
    message = input("Please input your message:\n")  # my name is vani
    message = list(message)
    return message

if ed == 'e':
    messages()
    random.Random(number).shuffle(message) # This is an operation you perform on the message so no need to assign message to it
    message = ''.join(message)
    print("Your encrypted message is: \n" + message + ".") #use . at the end so the user knows the last character is actually a space

else:
    messages()
    index_dm = list(range(len(message)))
    random.Random(number).shuffle(index_dm) #[2130]
    dd = dict(zip(index_dm, message))

    result = []
    for i in range(len(dd)):
        result.append(dd[i])
    message = ''.join(result)
    print("Your decrypted message is: \n" + message + ".")

