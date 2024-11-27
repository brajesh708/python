A1=str(input("Enter Your School Name"))
B1=str(input("Enter Your Center Code"))
C1=str(input("Enter Your School Code"))
D1=str(input("Enter Your Class"))
E1=str(input("Enter Your D.O.B"))
R1=str(input("Enter Your Roll no"))
P1=str(input("Enter Your Name"))
F1=str(input("Enter Your FName"))
M1=str(input("Enter Your MName"))
H1=int(input("Enter Hindi Mark"))
En=int(input("Enter English Mark"))
S1=int(input("Enter Sanskrit Mark"))
M2=int(input("Enter Math Mark"))
S2=int(input("Enter Science Mark"))
S3=int(input("Enter So.Science Mark"))
print("\t\tBOARDOF SECONDARY EDUCATION, M.P Bhopal")
print("\tHIGH SCHOOL CERTIFICATE EXAMINATION (10+2)2002, M.P Bhopal",end=" ")
print("\nSchool:",A1,end="")
print("\n\nRoll No:",R1,"\t\t\t\t\tCenter:",B1,end="")
print("\nName:",P1,"\t\t\t\tSchool:",C1,end="")
print("\nFName:",F1,"\t\t\tClass:",D1,end="")
print("\nMName:",M1,"\t\t\tD.O.B:",E1,end="")
print("\n\n\tSubcode   Sub Name  Maximun  Minimum  Obtain")
print("\t   H0001     Hindi     100      33      :",H1)
print("\t   E0001     English   100      33      :",En)
print("\t   S0001     Sanskrit  100      33      :",S1)
print("\t   M0001     Math      100      33      :",M2)
print("\t   SC001     Science   100      33      :",S2)
print("\t   SOS01     Sosal Sc. 100      33      :",S3)
if(H1<0 or H1>100):
  print("Invailid Marks")
elif(En<0 or En>100):
  print("Invailid Marks")
elif(S1<0 or S1>100):
  print("Invailid Marks")
elif(M2<0 or M2>100):
  print("Invailid Marks")
elif(S2<0 or S2>100):
  print("Invailid Marks")
elif(S3<0 or S3>100):
  print("Invailid Marks")
else:
 total=H1+En+S1+M2+S2+S3
 Per=total/6
 print("Total Marks:",total)
 print("Total Percentage:",Per)
 if(Per>=60):
  print("Pass in first division")
 elif(Per>=45):
  print("Pass in Second division")
 elif(Per>=33):
  print("Pass in third division")
 else:
  print("Fail")
