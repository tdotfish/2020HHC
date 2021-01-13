myfile = open("predicted.txt","r")
lines32 = myfile.readlines()
myfile.close

lines64 = [0] * int((len(lines32)/2))
counter = 0

for x in range(0,len(lines32),2):
  lines32[x] = int(lines32[x])
  lines32[x+1] = int(lines32[x+1])
  lines64[counter]=(lines32[x]|(lines32[x+1] << 32))
  counter += 1

outfile = open("rebuiltbitnonces.txt","w")
for y in range(len(lines64)):
  outfile.write("{}\n".format(lines64[y]))
outfile.close()
