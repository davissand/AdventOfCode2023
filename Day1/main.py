import re

with open('input.txt') as f:
    lines = f.readlines()

input= lines

cal_values=[]
cal_sum = 0
numbers =[]
for i in input:
    
    cal_string = (re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))',i))
    cal_values.append(cal_string)
    #cal_sum += int(cal_string[0] + cal_string[-1])
 
   # print(cal_sum)

for val in cal_values:
    for x in val:
        if x.isdigit():
            numbers.append(x)



# print(x)
# print(cal_sum)

def string_to_number(text):
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
        