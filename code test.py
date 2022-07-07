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
#---------------------------------------------------------------------------------------------------------------------------------
print("LECTURE 2 [multiple assignments]:")
#multiple assignments:multiple assignments allows us to assign multiple variables at the same time in one line of code

#normal method:
name="ASJ"
age=18
attractive=True
print(name)
print(age)
print(attractive)

#USING MULTIPLE STATEMENT
name="ASJ"
age=18
attractive=True
name,age,attractive="bro",21,True

name,age,attractive="ASJ",18,True
print(name)
print(age)
print(attractive)
#---------------------------------------------------------------------------------------------------------------------------------
print("LECTURE3[string methods]")

name="asj"
print(len(name))#len:gives the lenght of the string
print(name.find("s"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())#tells if the string has digits or not by returning true or false
print(name.isalpha())#tells if the string is alphabets or not by returning true or false
print(name.count("a"))
print(name.replace("a","A"))#replaces 'a' by 'A'
print(name*3)
#------------------------------------------------------------------------------------------------------------------
print("LECTURE 4[type cast]")

#TYPE CAST= convert the data type of a value into another data type
x=1   #int
y=2.0 #float
z="3" #str
print(x)
print(y)
print(z)

int(y)#converts it into int
int(z)
#to permanently change their values :
y=int(y)
z=int(z)
print(y)
print(z)
print(Z*3)
#similarly float()converts the datatype into a float


