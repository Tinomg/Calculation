def split_brackets(expression):
  
  try :
    end_index=expression.index(')')
    start_index=expression.rindex('(',0,end_index)
    return expression[slice(start_index+1,end_index)]
  except ValueError:
     # print ('No  more brackets')
      return expression
brack_input=list(input('Give expression with brackets:     '))
if split_brackets(brack_input):
    print(split_brackets(brack_input))