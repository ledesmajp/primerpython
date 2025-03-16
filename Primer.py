import random
import os
os.system('cls')

cpu = random.randint(1, 3)

while True:
    print("====================")
    print("Rock Paper Scissors")
    print("====================")
    print("1) ✊\n2) 🖐️\n3) ✌️")
    number = int(input("Pick a numer: "))
    while number == cpu:
        print(cpu)
        number = int(input("you tied, try again: "))
        cpu = random.randint(1, 3)      
        break
    print(cpu)
    if number == 1:
        if cpu == 2: print("You chose: ✊\nCPUchose: 🖐️\nCPU won!")
        else: print("You chose: ✊\nCPUchose: ✌️\nThe player won!")
        
    elif number == 2:
        if cpu == 3: print("You chose: 🖐️\nCPUchose: ✌️\nCPU won!")
        else: print("You chose: 🖐️\nCPUchose: ✊\nThe player won!")
        
    elif number == 3:
        if cpu == 2: print("You chose: ✌️\nCPU chose: 🖐️\nThe player won!")
        else: print("You chose: ✌️\nCPUchose: ✊\nThe player won!")

