for pypart in range(1,11):
# Function to demonstrate printing pattern
    def pypart(n):

        for i in range(0, n):
        
            # inner loop to handle number of columns
            # values changing acc. to outer loop
            for j in range(0, i+1):
            
                # printing stars
                print("* ",end="")
        
            # ending line after each row
            print("\r")
    # Driver Code
    n = 5
    pypart(n)
print(pypart)