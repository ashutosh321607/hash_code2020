import sys

def scorer(W,val,n):
  i  = 0
  x = 0
  value = val[i]
  while(value<W):
    x+=1
    i+=1
    value+=val[i]
  out = str(x) + "\n"
  for i in range(x):
    out+=str(i)+" "
  out+="\n"
  return out

# Driver code
arguments = len(sys.argv) - 1
for i in range(arguments):
  f = open(sys.argv[i+1],"r")
  W,n = map(int,f.readline().split())
  val=  list(map(int,f.readline().split()))
  out = open(sys.argv[i+1].split(".")[0]+".out","w+") 
  out.write(scorer(W, val, n))
  out.close()
  f.close() 
