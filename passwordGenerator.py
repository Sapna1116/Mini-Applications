import string
import random

def pwGenerator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = '#$%&@!*^'  # Specify the allowed punctuation characters

    pwLen = int(input("Enter the expected password length: "))

    # Ensure at least one character from each set
    pw = random.choice(s1) + random.choice(s2) + random.choice(s4)

    # Add other characters randomly
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)

    # Append characters to the password
    for _ in range(pwLen - 4):  # Subtract 4 for the characters already included
        pw += random.choice(s)

    pw += random.choice(s3)  # Fix indentation here

    print("Your generated password is:", pw)

pwGenerator()