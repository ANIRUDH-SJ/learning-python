print("LECTURE 9[logcal operators]")
#LOGICAL OPERATORS(and,or,not)=are used to check if two or more conditional statements are true  
temp=int(input("what is the temp outside?:"))
if temp>=0 and temp<=30:# for 'and' both the condition should be true
    print("the temp is good today")
    print("go outside")
elif temp<0 or temp>30:# for 'or' one condition should be satisfying 
    print("the temp is bad today!")
    print("stay inside")
#'not' conditional statement are used to check if one or more conditional statements
    
#BASICALLY BY USING not() we can change true to false and vice versa
