import requests
"""This is a code which sends requests to the manit result website and retrievs the name, branch, sch. no.
and CGPA of students in a certain range of scholar numbers, finally, it writes this info in a txt file"""

#Enter the scholar number to start from, and to end at, and the name of the file to be created
schStart = int(input("Enter starting scholar number: "))
schEnd   = int(input("Enter ending scholar number:   "))
filename = input("Enter filename to be made(along with .txt extension): ")
op = input("Enter C for CGPA, S for SGPA: ")
while op!='C' and op!='S':
    op = input("Invalid option! Enter C for CGPA, S for SGPA: ")
sem = input("Enter Semester (1/2/3/4/5/6/7/8): ")


if op=='C':
    op="CGPA"
elif op=='S':
    op="SGPA"

for num in range(schStart,schEnd+1):
    dic = {'scholar':num, 'semester':sem} #Change semester value as required!
    info = requests.post('http://dolphintechnologies.in/manit/accessview.php',data=dic)


    if info.status_code != 200:     #in case the request fails, take appropriate measures
        print("request failed for schno."+str(num)+", error=" + str(info.status_code))
        num-=1
        continue

    t = info.text #just doing this for ease of access/simple name
    f = open(filename,"a")
    if "Scholar No. not found" in t:    #if sch no not found, then just print it
        f.write("SchNo. %d not found\n" %(num))
    elif "Your Result has been withheld" in t:
        f.write("SchNo. %d the result has been withheld\n"%(num))
    else:
        start = t.find("Scholar No:")
        start += 116
        splice = t[start:]
        end = splice.find("   ")
        splice = splice[0:end]
        f.write("SchNo. %s " %(splice))
        
        start = t.find("Branch:")
        start += 112
        splice = t[start:]
        end = splice.find("   ")
        splice = splice[0:end]
        f.write("%s " %(splice))

        start = t.find(op)
        start+=15
        end=start+4
        splice = t[start:end]
        f.write("%s " %(splice))
        
        start = t.find("Name:")
        start += 110
        splice = t[start:]
        end = splice.find("   ")
        splice = splice[0:end]
        f.write("%s " %(splice) + "\n")
        f.close()
        

    print("Entry %d made" %(num-schStart+1))
print("Done!")

