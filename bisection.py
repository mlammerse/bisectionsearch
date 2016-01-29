#
balance = 320000
annualInterestRate = 0.2
#
#  
monthlyInterestRate = annualInterestRate/12.0
#
lowerBound = balance/12.0
upperBound = (balance * (1+monthlyInterestRate)**12)/12.0
#
monthlyPayment = (lowerBound+upperBound)/2.0
#
tempBalance=balance
#
while abs(tempBalance) >= 0.02: 
    tempBalance=balance
    
    for m in range (12):
        monthlyUnpaidBalance = tempBalance - monthlyPayment
        monthlyInterest = (annualInterestRate/12.0) * monthlyUnpaidBalance
        tempBalance = monthlyUnpaidBalance + monthlyInterest
    
    #print "tempBalance = " + str (tempBalance)
    
    if tempBalance > 0:
            lowerBound = monthlyPayment
    else:
            upperBound = monthlyPayment
     
    #print "lowerBound" + str (lowerBound)
    #print "upperBound" + str (upperBound)
       
    monthlyPayment = (lowerBound+upperBound)/2.0
    
    #print "here we go again"
    
print "Lowest Payment : " + str (round(monthlyPayment,2))

