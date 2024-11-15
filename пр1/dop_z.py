input_coordinates = input()
x, y = map(float, input_coordinates.split())

bit_code = ['0', '0', '0', '0']  

if y < 1:
    bit_code[0] = '1'  
if y < -x:
    bit_code[1] = '1'  
if x**2 + y**2 < 1:
    bit_code[2] = '1'  
if (x - 1)**2 + y**2 < 1:
    bit_code[3] = '1'  

bit_code_str = ''.join(bit_code)

print(bit_code_str)