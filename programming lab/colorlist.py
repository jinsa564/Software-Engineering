color1=input("enter a set of color(space separated):")
color2=input("enter a set of color(space separated):")
c1=set(color1.split())
c2=set(color2.split())
print("the difference between",c1,"and",c2,"is",c1.difference(c2))