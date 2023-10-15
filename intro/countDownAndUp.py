def countDownAndUp(number):
    print(number)
    if number == 0:
        # base case
        print('Reached base case')
        return
    else:
        # recursive case
        countDownAndUp(number - 1)
        print(number, 'returning')
        return
    
countDownAndUp(3)