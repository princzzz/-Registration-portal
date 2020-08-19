
#CSE student have 3 main CSE subject and 2 ECE subject and 1 HS subject
#ECE student have 3 main ECE subject and 2 CSE subject and 1 HS subject 
list1=[]
list2=[]
#for CSE main subjects are
CS201="CSE main"
CS310="CSE main"
SA310="Science"
#for ECE 
EC201="EC main"
EC310="EC main"
SA310="Science"
#These are the optional subject for the students according to their respective branch
CS231="CSE optional"
CS234="CSE optional"
CS506="CS optional"
EC231="EC optional"
EC234="EC optional"
EC506="EC optional"
#These are the Elective optional
HS708="Economics"
HS709="Political Science" 
def acadmic():
  print("Registration Portal")
  print("1. Registration")
  print("2. Details")
def registration():
    print("Wellocme to registration\n")
    name=input("Name : ")
    roll=input("Roll : ")
    sem=input("Semester : ")
    if roll[0]=='C':
        print("\n1.CS201(+1)\t2.CS310(+1)\t  3.SA310(+1)\n")
        print("Note-: One HS and Two EC subject is compulsory\n")
        print("1.HS708  Economics\t2.HS709 Political Science\n")
        print("1.EC231\t2.EC234\t3.EC506\n")
        hs=input("Hs course : ")
        if hs=='1':
            hs=HS708
        elif hs=='2':
            hs=HS709
        c1=input("EC first : ")
        if c1=='1':
            c1=EC231
        if c1=='2':
            c1=EC234
        if c1=='3':
            c1=EC506
        c2=input("EC second : ")
        if c2=='1':
            c2=EC231
        if c2=='2':
            c2=EC234
        if c2=='3':
            c2=EC506
        list1.append([name,roll,sem])
        list2.append([roll,hs,c1,c2])
        print("\nList One : \n",list1)
        print("\nList Two : \n",list2)
    if roll[0]=='E':
        print("\n1.EC201(+1)\t2.EC310(+1)\t  3.SA310(+1)\n")
        print("Note-: One HS and Two CS subject is compulsory\n")
        print("1.HS708  Economics\t2.HS709 Political Science\n")
        print("1.CS231]\t2.CS234\t3.CS506\n")
        hs=input("Hs course : ")
        if hs=='1':
            hs=HS708
        elif hs=='2':
            hs=HS709
        c1=input("CS first : ")
        if c1=='1':
            c1=CS231
        if c1=='2':
            c1=CS234
        if c1=='3':
            c1=CS506
        c2=input("CS second : ")
        if c2=='1':
            c2=CS231
        if c2=='2':
            c2=CS234
        if c2=='3':
            c2=CS506
        list1.append([name,roll,sem])
        list2.append([roll,hs,c1,c2])
       
       
    name=name+"     "+roll+"     "+"     "+sem+"     "+hs+"     "+c1+"     "+c2
    file=open("a.txt","a+")
    file.write(name)
    file.write("\n")
    file.close()
def details():
    print("Wellcome to details portal")  
    f=open("a.txt","r")
    print(f.read())
           
acadmic()

while 1:
    n=input("select option: ")
    if n=='1':
        registration()
    elif n=='2':
        details()
    elif n=='z':
        break
    else:
        print("wrong input")
   

