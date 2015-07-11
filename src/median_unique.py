elements = []
new_elements = []
medians = []

#----------------------MEDIAN FUNCTION --------------------------
def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]
#----------------------------------------------------------------
f = open("./tweet_input/tweets.txt", "r")
with f as inp:
     for line in inp:
          print len(set(line.split()))
          elements.append(len(set(line.split())))
f.close()

for z in range(0,len(elements)):
     medians.append(median(elements[0:z+1]))

g=open("./tweet_output/ft2.txt","w")
for item in medians:
     g.write("%s\n" % item)
g.close()

