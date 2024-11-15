input_string = input()

unique_digits = set()

for char in input_string:
    if char.isdigit():
        unique_digits.add(char)

if not unique_digits:
    print("NO")
else:
    sorted_digits = sorted(unique_digits)
    print(''.join(sorted_digits))
