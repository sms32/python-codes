source=open("a.txt","r")

destination=open("b.txt","w")

for line in source:

 destination.write(line)

source. close()

destination.close()
