"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
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
number = {}
for t in texts:
    number[t[0]] = 0
    number[t[1]] = 0
for t in calls:
    number[t[0]] = 0
    number[t[1]] = 0
print('There are',len(number),'different telephone numbers in the records.')
"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
