#operation


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