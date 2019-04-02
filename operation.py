#operation
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


user_expression=input('Write expresion')
split_expression=[]
number=''
for chart in user_expression:
    if chart.isdecimal() or chart=='.':
        number+=chart
    else:
        split_expression.append(number)
        split_expression.append(chart)
        number=''
split_expression.append(number)
print(split_expression)