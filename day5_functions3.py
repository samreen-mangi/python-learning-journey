def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

numbers = []

while True:
    choice = input("Enter a number or q to quit: ")

    if choice.lower() == "q":
        break

    num = int(choice)
    numbers.append(num)

print("\nResults:")
for n in numbers:
    print(n, "is", even_odd(n))
