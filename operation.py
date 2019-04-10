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
  
    bracket_patern=r"\([^\(\)]+\)"
    repl_string=(re.search(bracket_patern,expression).group()).strip('(').strip(')')
    expression=re.sub(bracket_patern,split_expression(repl_string),expression,1)
    return expression
# claculate 
def calculation(expr_string,operator):
  expr_list=expr_string.split(operator)
  return str(operation[operator](float(expr_list[0]),float(expr_list[1])))

#split simple expresion to operatos and numbers 
def split_expression(exspr_string):
  float_re='[0-9]*(\.?)[0-9]*'
  for operator in operation:
    oprerator_esc=operator
    if operator=="*" or operator=="+":
      oprerator_esc='\\'+operator
    operation_patern=float_re+oprerator_esc+float_re
    has_match=re.search(operation_patern,exspr_string)
    while has_match:
      exspr_string=(re.sub(operation_patern,calculation(has_match.group(),operator),exspr_string,1))
      has_match=re.search(operation_patern,exspr_string)
      
  return exspr_string




#start program
initial_expresion=result=user_input()
while True :
  try:
    finish_calculation=float(result)
    print(f"{initial_expresion}={finish_calculation}")
    break 

  except ValueError:
    if '(' in result and ')' in result:
      result=split_brackets(result)
    else:
      result=split_expression(result)
  
