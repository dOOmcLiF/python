import random

A, B, N = map(int, input().split())

array = [random.randint(A, B) for i in range(N)]
print(*array)  

max_sum = -1
result_pair = (0, 0)  

for i in range(N // 2):  
    left_index = i + 1
    right_index = N - i
    
    current_sum = array[i] + array[N - 1 - i]

    if current_sum % 2 == 0:
        if current_sum > max_sum:
            max_sum = current_sum
            result_pair = (left_index, right_index)  

if max_sum == -1:
    print(0, 0)
else:
    print(*result_pair)
