#Name: Malik Abdul Hadi
#Reg Number: 200901053
#BSCS-01
#LAB TASK
#QUESTION:Write a function in python that checks if parenthesis in the string are
#balanced or not. Use stack class;
class validequation: #Determining class
    stack = [] #initializing empty stack.
    def opening_closing(self,open,close): #determining a opening_closing function.
        if open=='[' and close==']': #Condition if opening bracket is [ and closing bracket is [ it will return true.
            return True
        if open=='(' and close==')':#Condition if opening bracket is ( and closing bracket is ) it will return true.
            return True
        if open=='{' and close=='}':#Condition if opening bracket is { and closing bracket is } it will return true.
            return True
        return False

    def Checking(self,Brackets):#determining a checking  function that will check the if the brackets are complete or not.
        for j in range(len(Brackets)): #Loop that will be from 1 to the size of the brackets the user will give.
            if Brackets[j]=='[' or Brackets[j]=='{' or Brackets[j]=='(': #As the are opening brackets they will be pushed into the stack.
                self.stack.append(Brackets[j])
            elif Brackets[j] == ']' or Brackets[j] == '}' or Brackets[j] == ')': #if they are closing brackets then,
                if self.opening_closing(self.stack[-1],Brackets[j] or len(self.stack)!=0):#It will pop that recently added closing bracket and will match from the existing last bracket if they are same they will be poped.
                    self.stack.pop()
                else:
                    print("Unbalanced")
                    return False #return false if they are not same.
        if len(self.stack)==0:
            print("Balanced")
            return True #If the lenght is equal to zero that means all of the brackets are being popped out and it will return true.
        else:
            return False
object = validequation() #Making object of the class.

print("Checking if the brackets are balanced or not.\n")
print("If they are balance it will return true, if they are not balanced it will return false.\n")
Brackets=input("Please enter your choice brackets: ")
print(object.Checking(Brackets)) #calling checking function

