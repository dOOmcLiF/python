input_data = input()

numbers = list(map(int, input_data.split()))

positive_count = sum(1 for number in numbers if number > 0)

print(positive_count)