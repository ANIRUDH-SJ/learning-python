print("LECTURE 12[nested loops]")
#nested loops= the "inner loop" will finish all of its iteration before finishing one iteration of the "outer loop"
rows=int(input("HOW MANY ROWS"))
columns=int(input("HOW MANY COLUMNS"))
symbol=input("Enter a symbol to use: ")
for i in range(rows):  #outer for loop
    for j in range(columns): #inner for loop
        print(symbol, end="")
    
