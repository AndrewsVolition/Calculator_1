# First project: Calculator

num_1 = input("Enter number: ")

while True:
    operator = input("Operation (+ - * / ^) or 'q' to quit: ")
    if operator == 'q':
        print(f"Answer: {num_1}")
        break
    num_2 = input("Enter number: ")
    if operator == '+':
        num_1 = float(num_1) + float(num_2)
        print(str(num_1))
    if operator == '-':
        num_1 = float(num_1) - float(num_2)
        print(str(num_1))
    if operator == '*':
        num_1 = float(num_1) * float(num_2)
        print(str(num_1))
    if operator == '/':
        num_1 = float(num_1) / float(num_2)
        print(str(num_1))
    if operator == '^':
        num_1 = float(num_1) ** float(num_2)
        print(str(num_1))
   
        

