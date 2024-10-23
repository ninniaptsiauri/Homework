# Number 1

with open ('text.txt', 'w') as file:
    for i in range(1, 1001):
        file.write(f"Line {i}\n")

with open('text.txt', 'r') as file:
    lines = file.readlines()
    print(f"Filled lines: {len(lines)}")




# Number 2 

lines = {
    2: 'Two',
    8: 'Eight',
    13: 'Thirteen',
    17: 'Seventeen',
}

with open('nums.txt', 'w') as numbers:
    for line in range(1, 21):
        if line in lines:
            numbers.write(f'{line}: {lines[line]}\n')

        else:
            numbers.write(f'{line}\n')





# Number 3

file1_info = ["First line - first file\n", "Second line - first file\n"]
file2_info = ["First line - second file\n", "Second line - second file\n"]

with open('file1.txt', 'w') as file1:
    file1.writelines(file1_info)

with open('file2.txt', 'w') as file2:
    file2.writelines(file2_info)

with open('mixed_files.txt', 'w') as mixed_file:
    with open('file1.txt', 'r') as file1:
        with open('file2.txt', 'r') as file2:
            mixed_file.writelines(file1.readlines())
            mixed_file.writelines(file2.readlines())

with open('mixed_files.txt', 'r') as mixed_file:
    content = mixed_file.read()
    print(content)




# Number 4

def is_palindrome(line):
    lines = ''.join(line.split()).lower()
    return lines == lines[::-1]

lines = ['Level\n', 'Home\n', 'Level', 'Python\n', 'Radar\n', 'World\n', 'Lool\n']

with open('palindrome.txt', 'w') as file:
    file.writelines(lines)

with open('palindrome.txt', 'r') as file:
    for line in file:
        if is_palindrome(line.strip()):
            print(line.strip())




# Number 5

def make_new_files(input_file):
     
    with open(input_file, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    file_count = (num_lines // 10) + (1 if num_lines % 10 else 0)

    for i in range(file_count):
        new_file_name = f'new_{i + 1}.txt'
        with open(new_file_name, 'w') as new_file:
            start = i * 10
            end = start + 10
            new_file.writelines(lines[start:end])

    print(f'Created files: {file_count}')

make_new_files('text1.txt')




# Number 6 

def delete_clear_lines(input_file, input_file2):

    with open(input_file, 'r') as file:
        lines = file.readlines()

    remove_clear_lines = [line for line in lines if line.strip()]

    with open(input_file2, 'w') as file:
        file.writelines(remove_clear_lines)

    
delete_clear_lines('story.txt', 'story1.txt')


    