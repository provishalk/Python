try:
       f=open("input1.txt","r")
       while True:
               line=f.readline()
               if line=='':break
               print (line, end='')
except FileNotFoundError:
       print ("File is not found")
else:
       f.close()