# classroom hall monitor challenge - Vanessa Rodriguez, Ayelen Cardenas

status0 = "Ok"
status1 = "warning"
status2 = "flagged"

# 1. Create Hall Pass List - Ayelen Cardenas

student_names = [   ]   
student = input("What is your name?: ")
student_names.append(student)
name_count = student_names.count(student)

# 2. Loop - Vanessa Rodriguez



# 3. Classify each student - Vanessa Rodriguez

new_status = status0
time = [   ]
minutes = int(input("How long have you been in the hallway for?: "))
time.append(minutes)
if minutes >= 0 and minutes <= 5:
    new_status = status0
elif minutes >= 6 and minutes <= 10:
    new_status = status1
else:
    new_status = status2  

student = input("Enter the student's time: ")

for student in status0:
    if minutes >= 0 and minutes <= 5:
        print(f"This student is {status0}.")

for student in status1:
    if minutes >= 6 and minutes <= 10:
        print(f"This student got a {status1}.")

for student in status2:
    if minutes >= 11:
        print(f"This student got {status2}.")



# 4. Add a special rule -  Ayelen Cardenas
special_rule = [  ]
if minutes>10 or name_count>1:
    new_status = status2
    if minutes>10:
        special_notes = "spent over 10 min outside"
    elif name_count>1:
     special_notes = "duplicate name detected"
else:
    special_notes = "N/A"
    
special_rule.append(special_notes)

status = [   ]
status.append(new_status)

print(student_names)
print(status)
print(special_notes)


a = [
    [student_names[0], status[0], special_notes[0]]
]

a.extend(student_names)
a.extend(status)
a.extend(special_rule)

header = ['Names', 'Status', 'Special Notes']
print(f"{header[0]:<10}   {header[1]:<15}    {header[2]:<18}")
print("-"*40)
for row in a:
    print(f"{row[0]:<10}   {row[1]:<15}    {header[2]:<18}")



