from random import *
import string

class NeedleInHaystack:

   def __init__(self, needle, haystack):
       self.needle = needle
       self.haystack = haystack

   def stringMap(self, s):
      stringMap = {}
      for letter in s:
         occurences = stringMap.setdefault(letter, 0)
         stringMap[letter]=occurences+1
      return stringMap

   def findOccurrences(self):
      needlesFound = []
      needlelength = len(self.needle)
      #create a map of the needle, with occurrences of each letter
      needlemap = self.stringMap(self.needle)

      for i,letter in enumerate(self.haystack):
         #create that needle for each letter plus the length of the needle
         posNeedle = self.haystack[i:i+needlelength]
         #no need to compare if not equal length
         if len(posNeedle) == needlelength:
             posNeedleMap = self.stringMap(posNeedle)
             #compare dictionaries and if they are equal we've found a match
             if needlemap == posNeedleMap:
                 #print "found {0} in {1} ".format(posNeedle,haystack)
                 needlesFound.append(posNeedle)
      return needlesFound


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(choice(letters) for i in range(length))

if __name__ == "__main__":

    #create a randome string of letters using method randomword()
    haystack = randomword(50)
    #concat the haystack with itself backwards so there will be 2 occurrences found
    haystack = haystack + haystack[::-1]

    randomint = randint(0,len(haystack))
    #create a needle using a random substring
    needle   = haystack[randomint:randomint+3]

    print "haystack:{0}".format(haystack)
    print "needle:{0}".format(needle)

    needleInHay = NeedleInHaystack(needle, haystack)
    print needleInHay.findOccurrences()



