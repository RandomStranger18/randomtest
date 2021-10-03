#PR
def power(x, y): 
      
    if y == 0: 
        return 1
    if y % 2 == 0: 
        return power(x, y // 2) * power(x, y // 2) 
          
    return x * power(x, y // 2) * power(x, y // 2) 
  
# Function to calculate order of the number 
def order(x): 
  
    # Variable to store
          
    return n
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
      
# Driver code 
string = 'The quick brown fox jumps over the lazy dog.'
if(ispangram(string) == True): 
    print("Yes") 
else: 
    print("No") 
