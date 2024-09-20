# Read a number from the user and print the Lucky digit of the user where the luoky digit is found by finding the sum of digits of the givon number and repeat the algorithm until single digit number is arrived789 24 6
def find_lucky_digit(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

number = int(input("Enter a number: "))
lucky_digit = find_lucky_digit(number)
print(f"The lucky digit is: {lucky_digit}")
