def print_table(num):
    for i in range(1, 21):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number: "))
print_table(number)