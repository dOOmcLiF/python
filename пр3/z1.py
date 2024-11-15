input_data = input()
numbers = list(map(int, input_data.split()))

for i in range(len(numbers) - 1):
    if (numbers[i] > 0 and numbers[i + 1] > 0) or (numbers[i] < 0 and numbers[i + 1] < 0):
        print(numbers[i], numbers[i + 1])
        break