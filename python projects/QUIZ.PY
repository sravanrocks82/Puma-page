print('welcome to Quiz game')
answer=input('enter are you interested to play?')
marks=0
if answer!='yes':
    quit()
else:
    print('hey!here comes your first question')

print('who is our prime minister')
answer1=input()
if answer1=='pmmodi':
    marks+=1
    print('your answer is correct')
else:
    print('your is answer is wrong')
    
    
print('what is our national game')
answer1=input()
if answer1=='hockey':
    marks+=1
    print('your answer is correct')
else:
    print('your is answer is wrong')

    
print('what is our national bird')
answer1=input()
if answer1=='peacock':
    marks+=1
    print('your answer is correct')
else:
    print('your is answer is wrong')

    
print('what is opposite of love')
answer1=input()
if answer1=='hate':
    marks+=1
    print('your answer is correct')
else:
    print('your is answer is wrong')

    
print('what is the capital of andhrapradesh')
answer1=input()
if answer1=='we only dont know':
    marks+=1
    print('your answer is correct')
else:
    print('your is answer is wrong')

print('thank you for your patience')
print(f'{marks} your score')
5