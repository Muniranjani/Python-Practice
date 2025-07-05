#f=open("C:\\Users\\R.MUNIRANJANI\\Documents\\PYTHON\\myfile.txt",'w')
#f.write("Hello Java")
#f.close()

# f=open("C:\\Users\\R.MUNIRANJANI\\Documents\\PYTHON\\myfile.txt",'a')
# f.write(" Hiii prixxx...how are youuu????")
# f.close()

import os
filename=input("Enter file name: ")
if os.path.isfile(filename):
    print("yes present")
    f=open(filename,"r")
    output=f.read()
    print(output)
else:
    print("no, not present")
