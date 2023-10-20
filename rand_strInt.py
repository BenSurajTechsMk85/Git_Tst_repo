import random
import string
def rand_string(length):
    rand_str = "".join(random.choice(string.ascii_lowercase
    +string.ascii_uppercase
    +string.digits) for i in range(length))

    return rand_str
print(rand_string)
print(random.random(),end="")
