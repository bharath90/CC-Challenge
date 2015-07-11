with open("./tweet_output/ft1.txt","w") as g:
     f = open("./tweet_input/tweets.txt", "r")
     from collections import Counter
     wordcount = Counter(f.read().split())
     for item in wordcount.items():
          print ("{}\t{}".format(*item))
          g.write("{}\t{}\n".format(*item))
          f.close()
g.close()
