import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]
password = []

num_let = int(input("How many letters would you like in your password?\n: "))
num_num = int(input("How many numbers?\n: "))
num_sym = int(input("How many symbols?\n: "))

total_char = num_let + num_num + num_sym
print(f"character count: {total_char}")
if total_char <= 20:
    while num_let+num_num+num_sym > 0:

        random_num = random.randint(1,3)
        if random_num == 1 and num_let >0:
            password.append(random.choice(letters))
            num_let -= 1
        elif random_num == 2 and num_num > 0:
            password.append(random.choice(numbers))
            num_num -= 1
        elif random_num == 3 and num_sym > 0:
            password.append(random.choice(symbols))
            num_sym -= 1

else:
    print("password is too long")

final_password = ""
for char in password:
    final_password += char
print(final_password)