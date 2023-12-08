file = open('day1/input.txt', 'r')
lines = file.readlines()

numlist = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

sum = 0
for line in lines:
    fixed_line = line
    for num, value in numlist.items():
        fixed_line = fixed_line.replace(num, f'{num}{value}{num}')
    digits = [x for x in fixed_line if x.isdigit()]
    first_digit = digits[0]
    last_digit = digits[-1]
    number = int(first_digit + last_digit)
    sum += number
print(sum)