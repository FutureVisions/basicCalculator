print('Select and operation to use')
print('1: ADD')
print('2: Subtract')
print('3: Multiply')
print('4: Divide')

operation = input('select one of the operations: ')

if operation == '1':
  print('add your numbers')
    # code for add
  user_num1 = int(input('select the first number you would like to add: '))
  user_num2 = int(input('select the second number you would like to add: '))
  result = user_num1 + user_num2  
  print('{} + {} = {}'.format(user_num1,user_num2,result))
elif operation == '2':
    # code for subtract
  print('subtract your numbers')
  user_num1 = int(input('select the first number you would like to subtract: '))
  user_num2 = int(input('select the second number you would like to subtract: '))
  result = user_num1 - user_num2  
  print('{} - {} = {}'.format(user_num1,user_num2,result))
elif operation == '3':
  # code for multiply
  print('multiply your numbers')
  user_num1 = int(input('select the first number you would like to multiply: '))
  user_num2 = int(input('select the second number you would like to multiply: '))
  result = user_num1 * user_num2  
  print('{} x {} = {}'.format(user_num1,user_num2,result))
elif operation == '4':
  # code for divide
  print('divide your numbers')
  user_num1 = int(input('select the first number you would like to divide: '))
  user_num2 = int(input('select the second number you would like to divide: '))
  result = user_num1 / user_num2  
  print('{} ÷ {} = {}'.format(user_num1,user_num2,result))

