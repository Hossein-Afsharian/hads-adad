import random

pc_number = random.randint(0,20)
guess=0
while True:

    user_number = int(input("enter number:"))
    guess+=1
    if user_number==pc_number:
        print("nice")

        break
    if user_number>pc_number:
        print("adad kochak shavad")
    if user_number<pc_number:
        print("adad bozorg shavad")

print(pc_number , guess)