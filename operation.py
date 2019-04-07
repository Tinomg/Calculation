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
  
  bracket_patern="\([^\(\)]+\)"
  brack_string=re.match(bracket_patern,expression)
  return brack_string

# claculate 
def calculation(expr_string,operator):
  expr_list=expr_string.split(operator)
  return operation[operator](expr_list[0],expr_list[1])

#split simple expresion to operatos and numbers 
def split_expression(exspr_string):
    float_re="([0-9]*\.?[0-9])"
    operator="(\\"+"+"+")"
    operation_patern="^"+float_re+operator+float_re+"$"
    print(operation_patern)
    result=re.search(operation_patern,exspr_string)
    return result 

#start program
raw_expression=user_input()
while split_brackets(raw_expression):
  brack_expression=split_brackets(raw_expression).group()