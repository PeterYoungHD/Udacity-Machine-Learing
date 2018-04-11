"""
Intro to Python Lab 1, Task 3

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

codes = []
num1 = 0
num2 = 0
for t in calls:
    num = ''
    p = 0
    if t[0][0:5] == '(080)':
        num1 = num1 + 1
        if t[1][0:5] == '(080)':
            num2 = num2 + 1
        if t[1][0] == '(':
            for z in t[1]:
                p = p+1
                if z == ')':
                    break
            num = t[1][0:p]
        elif (t[1][0] == '9') or (t[1][0] == '8') or (t[1][0] == '7'):
            num = t[1][0:4]
    if (num not in codes) and (num != ''):
        codes.append(num)
codes = sorted(codes)
print("The numbers called by people in Bangalore have codes:")
for n in codes:
    print(n)
print(round(num2 / num1 * 100,2),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
