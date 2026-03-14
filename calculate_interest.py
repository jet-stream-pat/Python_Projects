
#This is an interest Calculator

print('Interest Calculator:') 
amount = float(input('Please enter a Principal amount ? ')) 
roi = float(input('What id the Rate of Interest ? ')) 
yrs = int(input('What is the Duration (no. of years) of the loan? ' ))

total = (amount * pow(1 + (roi/100), yrs)) 
interest = total - amount

print('\n Interest received = %0.2f' %interest) 

