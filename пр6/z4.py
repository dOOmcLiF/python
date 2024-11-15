n = int(input())

possible_numbers = set(range(1, n + 1))

while True:
    question = input()

    if question == "HELP":
        break

    answer = input().strip()

    numbers_in_question = set(map(int, question.split()))

    if answer == "YES":
        possible_numbers.intersection_update(numbers_in_question)
    elif answer == "NO":
        possible_numbers.difference_update(numbers_in_question)

result = sorted(possible_numbers)
print(" ".join(map(str, result)))
