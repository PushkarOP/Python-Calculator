def sum(x, y):
       return x+y
       
def subtract(x, y):
        return x-y
 
def multiply(x, y):    
       return x*y
  
def divide(x, y):  
       return x/y
while True:      
 print("Welcome To Python Calculator\n==========================================")
 print("Select operation.")
 print("1.Add")
 print("2.Subtract")
 print("3.Multiply")
 print("4.Divide")
 choice = input("Enter choice(1/2/3/4): ")
 num1 = int(input("Enter The First Value :"))
 num2 = int(input("Enter The Second Value :"))
 if choice == '1':
    print(num1, "+", num2, "=", sum(num1, num2))
 elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
 elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
 elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
 elif choice <= '999999':
    print("Plese Select Valid Choice")
 print("==========================================")
 choice2 = input("Do You Want To Continue Yes/No?")
 if choice2 == "No":
   print("Thanks For Using Calculator")
   break 
 elif choice2 == "no":
   print("Thanks For Using Calculator")
   break 
 print("==========================================")