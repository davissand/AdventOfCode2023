import re

with open('input.txt') as f:
    lines = f.readlines()

input= lines

cal_values=[]
cal_sum = 0
numbers =[]

def string_to_number(text):
    if text.isnumeric():
        return int(text);

    match text:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        
#recorriendo la lista de los datos de entrada
for i in input:
    #searching for digits or numbers in text and adding the list of numbers found to cal_string
    cal_string = (re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))',i))

    #adding the first and last value of the list and concatenating the individual numbers in a 2 digits number
    cal_values.append(int(str(string_to_number(cal_string[0]))+ str(string_to_number(cal_string[-1]))))

total = 0
for val in cal_values:
    total += val

print(total)
print(sum(cal_values))
