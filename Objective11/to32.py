myfile = open("64bitnonces.txt","r")
lines64 = myfile.readlines()
myfile.close

lines32 = [0] * (len(lines64)*2)
counter = 0

for x in range(len(lines64)):
  lines64[x]=int(lines64[x])
  lines32[counter] = lines64[x] & 0xFFFFFFFF
  counter+=1
  lines32[counter] = lines64[x] >> 32
  counter+=1

outfile = open("32bitnonces.txt","w")
for y in range(len(lines32)):
  outfile.write("{}\n".format(lines32[y]))
outfile.close()
