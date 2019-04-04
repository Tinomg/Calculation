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
#allowed characters
allowed_chars=('0','1','2','3','4','5','6','7','8','9','*','/','+','-','(',')','.')
#Uncorect mesage function
def error_message(uncorrect_char):
    return (f'Not corect input -> {uncorrect_char}')
user_expression=input('Write expresion')
split_expression=[]
number=''


#disasemblig brackets and returning star,end and slice for operation
def split_brackets(expression):
  
  try :
    end_index=expression.index(')')
    start_index=expression.rindex('(',0,end_index)
    return expression[slice(start_index+1,end_index)],start_index,end_index
  except ValueError:
     # print ('No  more brackets')
      return expression,start_index,start_index