a = float(input())
b = float(input())
operation = str(input("Enter your chice"))
match operation:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        print(a / b)
    case '//':
        print(a // b)
    case '%':
        print(a % b)
    case '**':
        print(a ** b)    
    case _ :
        print("enter a valid choice")                        