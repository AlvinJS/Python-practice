#Group 3
# write a program that 
# Input: ask users for 10 verbs 
# Output: create a continuous present tense of the verbs

# creating an empty list

verb = []

 

# number of elements as input

print("Please enter ten verbs")

 

# iterating till the range

for i in range(1, 4):
    print("Enter verb number",i,":")
    ele = input()

    #if the word ends with an 'e'

    lastIndex = len(ele) -1
    if ele[lastIndex] == "e":
        ele = ele[:-1]     
    ele = ele + "ing"

    verb.append(ele) # adding the element

#printing verbs    
print("--------------------------------------")
print("List of verbs in present continuous") 
print("--------------------------------------")  

for i in verb:
 print(i)