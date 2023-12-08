file = open('day1/input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    digits = [x for x in line if x.isdigit()]
    first_digit = digits[0]
    last_digit = digits[-1]
    number = int(first_digit + last_digit)
    sum += number
print(sum)