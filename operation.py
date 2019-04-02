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

# Getting adn checking user input
#allowed characters
allowed_chars=('0','1','2','2','4','5','6','7','8','9','*','/','+','-','(',')','.')
#Uncorect mesage function
def error_message(uncorrect_char):
    return (f'Not corect input {uncorrect_char}')
user_expression=input('Write expresion')
split_expression=[]
number=''
for chart in user_expression:
    if chart in allowed_chars:
      if chart.isdecimal() or chart=='.':
        number+=chart
      else:
        split_expression.append(number)
        split_expression.append(chart)
        number=''
    else :
        print(error_message)
split_expression.append(number)
print(split_expression)