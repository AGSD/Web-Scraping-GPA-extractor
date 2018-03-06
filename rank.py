#A prog which reads the file given, and tries to find all people with score more that
#value stored in my, it displays their names, and finally tells rank of person with CGPA stored in my
filename = input("Enter file name:   ")
pointer = float(input("Enter your pointer: "))
#numofstu = int(input("Enter the last roll no. eg 110/99 etc: "))

f = open(filename,"r")
my = pointer

rank=1
print("People with pointers better than yours:\n")
while True:
    splice = f.readline()
    if splice=='':
        break
    if 'not found' not in splice and 'withheld' not in splice:
        splice = splice[10:]
        n = splice.find(".")
        s = splice[n-1:n+3]
        c=float(s)
        if c > my:
            print(c,splice[n+3:])
            rank+=1
    

print("Your rank: ",rank)
    
