print("LECTURE 1 [variables]:")
#STRING:
first_name="bro"
last_name="code"
full_name=first_name+" "+last_name
print("hello"+full_name)
#type() gives the type of datatype

#INT:
age=21
print(age)
age +=1   #{imp note: there is no space between '+' and '='}
print("your age is:"+str(age))   #{str()converts the data inside it into a string}
#{type()tells us what is the type of data inside it}
#{we can only concatenate strings with strings}

#FLOAT:
height=250.5
print(height)
print(type(height))
print("your height is:"+str(height)+"cm")

#BOOLEAN(can store only true or false value):
human=False #here 'f' is caps as it is a keyword
print(human)
print(type(human))
print("Are you a human: "+str(human))
