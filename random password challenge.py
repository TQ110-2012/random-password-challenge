import random
import string

length = int(input("Enter the desired password length: "))

all_chars = string.ascii_letters + string.digits

password_list = [random.choice(all_chars) for _ in range(length)]

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your generated password is: {password}")
