def split_brackets(expression):
  
  try :
    end_index=expression.index(')')
    start_index=expression.rindex('(',0,end_index)
    return expression[slice(start_index+1,end_index)],start_index,end_index
  except ValueError:
     # print ('No  more brackets')
      return expression,start_index,start_index
brack_input=input('Give expression with brackets:     ')




print(split_brackets(brack_input))




