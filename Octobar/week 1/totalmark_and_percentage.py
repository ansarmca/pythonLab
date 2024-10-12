#Python program to calculate total mark and percentage of 5 subject

sub1= int(input("enter marks of Python :"))
sub2= int(input("enter marks DFCA :"))
sub3= int(input("enter marks of Maths :"))
sub4= int(input("enter marks of C Programming :"))
sub5= int(input("enter marks of data structure :"))

total = (sub1+sub2+sub3+sub4+sub5)
percentage = (total/500)*100

print("Total is : ",total)
print("Percentage is: ",percentage)
