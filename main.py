# classroom hall monitor challenge - Vanessa Rodriguez, Ayelen Cardenas
# 1. Create Hall Pass List - Ayelen Cardenas
student_names = [   ]   
student = input("What is your name?: ")
student_names.append(student)
name_count = student_names.count(student)

# 2. Loop 
# student = input("Enter the student's time")

# while student == ("")

# 3. Classify each student - Vanessa Rodriguez

status0 = "Ok"
status1 = "warning"
status2 = "flagged"
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


# 4. Add a special rule -  Ayelen Cardenas

if minutes>10 or name_count>1:
    new_status = status2
if minutes>10:
    special_notes = "spent over 10 min outside"
if name_count>1:
    special_notes = "duplicate name detected"

status = [   ]
status.append(new_status)

data_list = [student_names, status, special_notes]
header = ["Name", "Status", "Special Notes"]
print(f"{header[0]:<10} {header[1]:<15}")
print("-"*25)
for row in data_list:
    print(f"{row[0]:<10} {row[1]:<15}")
