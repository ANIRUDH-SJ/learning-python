print("LECTURE 7[STRING SLICING]")
#SLICING- is used to create a substring by extracting elements from another string we can use either indexing[] or slice()for slicing
#[start:stop:step] NOTE:here the indexing starts from zero and the stop parameter i exclusive
name="bro code"
first_name= name[0:2]
print(first_name)
last_name=name[4:8]
print(last_name)
funky_name=name[0:8:2]
print(funky_name)
reversed_name=name[::-1]
print(reversed_name)

website="http://google.com"
slice=slice(7,-4)# here stop parameter has negative index as it is counted from the end 
print(website[slice])



