# Project to sort the list's objects in ascending order

object_List = [] #the List which will store the Objects

for n in range (10): #The Loop to get 10 input
    Entered_object = input("Please type any object : ")
    object_List.append(Entered_object)

object_length = len(object_List)
i = 0
while(i < object_length): 
    j = i + 1
    while(j < object_length):
        if(len(object_List[i]) > len(object_List[j])): #if condition to compare the retrieved elements
            temp = object_List[i]
            object_List[i] = object_List[j]
            object_List[j] = temp
        j = j + 1
    i = i + 1

print("Elements is Ascending Order : ", object_List)