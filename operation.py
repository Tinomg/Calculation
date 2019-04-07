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
    brack_string=re.search(bracket_patern,expression)
    return brack_string
  else:
    return expression

# claculate 
def calculation(expr_string,operator):
  expr_list=expr_string.split(operator)
  return operation[operator](float(expr_list[0]),float(expr_list[1]))

#split simple expresion to operatos and numbers 
def split_expression(exspr_string,operator):
    float_re="([0-9]*\.?[0-9])"
    operator_decoration="(\\"+operator+")"
    operation_patern="^"+float_re+operator_decoration+float_re+"$"
    try:
      result=(re.search(operation_patern,exspr_string)).group()
    except AttributeError:
      return None 
    return result




#start program
raw_expression=user_input()
while split_brackets(raw_expression):

  for operator in operation.keys():
    inbracket_string=split_brackets(raw_expression).group().strip('(').strip(')')
    while split_expression(inbracket_string,operator):
      splited_string=split_expression(inbracket_string,operator)
      print(calculation(splited_string,operator))
  if  split_brackets(raw_expression)==raw_expression:
    break
