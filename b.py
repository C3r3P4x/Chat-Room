print("use alphabets, letters and underscores only  (max length 14) \nEnter your name: ")
while True:
    name = input()
    count = 0
    for char in name:
        if char.isdigit()  or char.isalpha() or char == "_":
            count += 1
    if count == len(name):
        print(f"welcome {name}")
        break
    else:
        print("Invalid name, try again\nEnter your name : ")
