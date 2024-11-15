input_string = input()

trimmed_string = input_string.strip()

formatted_words = []
current_word = ""

for char in trimmed_string:
    if char == ' ':
        if current_word:
            formatted_words.append(current_word)
            current_word = ""
    elif char in {'.', ','}:
        if current_word:
            formatted_words.append(current_word)
            current_word = ""
        formatted_words.append(char)
    else:
        current_word += char

if current_word:
    formatted_words.append(current_word)

final_string = ""
for word in formatted_words:
    if final_string and word not in {'.', ','}:
        final_string += ' '
    final_string += word

print(final_string.strip())