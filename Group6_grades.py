# Function to hold grade corresponding to score
def determinegrade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 65 <= score <= 79:
        return 'B'
    elif 64 <= score <= 64:
        return 'C'
    elif 50 <= score <= 54:
        return 'D'
    else:
        return 'F'
    
count = 0
# Use range(10) because function should repeat 10 times
for name in range(10):  
# Ask user to input name which is stored in name as a string
    name = str(input('Please enter your name: '))
# Ask user to input score which is stored in grade as an integer
    grade = int(input('What is your score? '))
# count shows you which iteration you are on
    count = count + 1
    print(count,'Hello',name,'your grade is:',determinegrade(grade))

