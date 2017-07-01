while True:
    print('this is a mini calculator')
    print('it takes only two integers')
    print('for addition input +')
    print('for subtraction input -')
    print('for division input /')
    print('for  multiplication input *')
    print('for power input **')
    print('for modulous input %')
    print('input exit to quit app')
    user=input('press enter to continue:')
    if user == 'exit':
        print('goodbye')
        break

    
    print('input your value below')
    a=int(input('first value:'))
    b=int(input('second value:'))
    #if isinstance(a,str) or isinstance(b,str):
        #print('invalid input,it must be an integer')
        #break
    #if isinstance(a,int) or isinstance(b,int):
        #continue
    
    print('which operation do u want?')
    user_input=input('')
    if   user_input == '-':
        result = a - b
        message=('your answer is %d')
        print(message % result)
    elif user_input == '+':
        result = a + b
        message=('your answer is %s')
        print(message % result)
    elif user_input == '/':
         result = a / b
         message=('your answer is %s')
         print(message % result)
    elif user_input == '*':
         result = a * b
         message=('your answer is %f')
         print(message % result)
    elif user_input == '**':
         result = a ** b
         message=('%s raise to the power of %s is %s')
         print(message % (a,b,result))
    elif user_input == '%':
         result = a % b
         message=('the modulus of %r in %r is %r')
         print(message % (a,b,result))
    print('do you want to perform another operation?')
    way_out=input(':')
    if way_out == 'yes':
        continue
    elif way_out == 'no':
        print('thanks for your time,GOODBYE')
        break


    
