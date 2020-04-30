"""currently relearning the control structure lessons in py3 on sololearn"""

x = True
num1 = 0
num2 = 0
def get_answer():
  num1 = float(input("enter the first number"))
  num2 = float(input("input the second number"))
while x == True:
  user_input = input("to use this calulator, you must enter the following options exactly:/nadd/nsubtract/nmultiply/ndivide/nandquit/nso, what do you want to do?")
  if user_input == "add":
      get_answer()
      result = num1 + num2
  elif user_input == "subtract":
      get_answer()
      result = number1 - number2
  elif user_input == "multiply":
      get_answer()
      result = number1 * number2
  elif user_input == "divide":
      get_answer()
      result = number1 / number2
  else: print("bye")
print(result)
x = False
