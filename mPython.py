number_count = 0
even_count = 0
odd_count = 0
numbers_dict = {}

while True:
    user_input = input("Enter a number (or 'exit' to end): ")

    if user_input.lower() == 'exit':
        break

    try:
        number = int(user_input)
        number_count += 1

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        numbers_dict[number_count] = {'number': number, 'even': number % 2 == 0}
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Total numbers entered: {number_count}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print("Numbers and their even/odd status:")
for count, data in numbers_dict.items():
    print(f"{count}: {data['number']} - {'Even' if data['even'] else 'Odd'}")
     
