
#calculating slope using two points and make into an un-simplified equation

print("We're going to be calcuting slope by using two points and making an equation\n")

#getting x-values and y-values
xone = input("First x-value:")
yone = input("First y-value:")

xtwo = input("Second x-value:")
ytwo = input("Second y-value:")

#calculating slope
slope = (int(ytwo) - int(yone)) / (int(xtwo) - int(xone))
print("\nSlope is", slope)

#making into an un-simplified equation
print("\n Un-simplified equation is: \n y -",yone,"=",slope,"(x -",xone,")")

#yay you should have an answer

#Sample input values with expected output
#xone=-12 yone=-2    xtwo=21 ytwo=-7
#expected output is -0.15151515151515
#expected equation is y - -2 = -0.15151515151515(x - -12)

#Another example
#xone=7 yone=4     xtwo=5 ytwo=14
#expected output is -5
#expected equation is y - 4 = -5(x-7)