def calculate_score(grades):
    sorted_grades = sorted(grades)
    
    min_grade = sorted_grades[0]
    max_grade = sorted_grades[-1]
    
    remaining_grades = sorted_grades[1:-1]
    
    final_score = sum(remaining_grades) / len(remaining_grades)
    
    return min_grade, max_grade, final_score

input_grades = input()
grades = list(map(int, input_grades.split()))

min_grade, max_grade, final_score = calculate_score(grades)
    
print(min_grade, max_grade)
print(f"{final_score:.2f}")