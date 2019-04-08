import re


# operation
def mult(first_num,second_num):
    return first_num*second_num
def dev(first_num,second_num):
    try:   
      return first_num/second_num
    except ZeroDivisionError:
        print("Zero divide error !")
        return None
def add(first_num,second_num):
    return first_num+second_num
def sub(first_num,second_num):
    return first_num-second_num
operation={'*':mult , '/':dev , '+':add , '-':sub}

# Getting user input
def user_input():
  user_expression=input('Write expresion')
  return user_expression


#disasemblig brackets and returning star,end and slice for operation
def split_brackets(expression):
  if '(' in expression and ')' in expression:
    bracket_patern=r"\([^\(\)]+\)"
    brack_string=re.sub(bracket_patern,split_expression(expression),expression)
    return brack_string
  else:
    return expression

# claculate 
def calculation(expr_string,operator):
  expr_list=expr_string.split(operator)
  return operation[operator](float(expr_list[0]),float(expr_list[1]))

#split simple expresion to operatos and numbers 
def split_expression(exspr_string):
    float_re=r'([0-9]*(\.?)[0-9])'
    print(float_re)
    for operator in operation:
      operator_decoration="(\\"+operator+")"
      operation_patern=r"^"+float_re+operator_decoration+float_re+"$"
      print(operation_patern)
      while re.search(operation_patern,exspr_string):
        result=(re.sub(operation_patern,calculation(exspr_string,operator),exspr_string))
      
    return result




#start program
result="2+3+3+3"
try:
  print(float(result))

except ValueError:
  while True :
    result=split_expression(result)
  
