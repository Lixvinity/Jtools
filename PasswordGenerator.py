import random
import string
import time


Debug = True

Characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


# Debug output 1
if Debug == False:
    print(Characters)

RandomKey = input('put in long gibberish to make a more secure and random password')

random.seed(hash(RandomKey))

PasswordLength = int(input('how long do you want the password to be?'))

password = "".join(random.sample(Characters, PasswordLength))

print('Your brand new secure password is ' + password)

time.sleep(60)
