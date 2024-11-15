def filter_dogs_by_age(input_file, output_file, K):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    dogs = lines[1:]
    filtered_dogs = []

    for dog in dogs:
        name, age_str, breed = dog.split()
        age = int(age_str)

        if age < K:
            filtered_dogs.append(dog.strip())

    with open(output_file, 'w') as f:
        for dog in filtered_dogs:
            f.write(dog + '\n')
        f.write(str(len(filtered_dogs)) + '\n')


input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r') as f:
    K = int(f.readline().strip())
filter_dogs_by_age(input_file, output_file, K)
