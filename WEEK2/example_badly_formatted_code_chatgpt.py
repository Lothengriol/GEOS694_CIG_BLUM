import math,sys,os
from collections import defaultdict


DATA_POINTS=[(1,2),(2,4),(3,9),(4,16),(5,25)]

def ProcessData(dataPoints,ScaleFactor=1,verbose=False): results=[];total=0
 for i in range(0,len(dataPoints)):
  x=dataPoints[i][0];y=dataPoints[i][1]
  newY=y*ScaleFactor;results.append((x,newY));total+=newY
 if verbose==True: print("Processed",len(dataPoints),"points with scale",ScaleFactor,"total is",total)
 return results,total

class analyzer:
 def __init__(self,name="defaultAnalyzer",threshold=10,data=[]):
  self.Name=name
  self.threshold=threshold
  self.data=data

 def addData(self,point): self.data.append(point)

 def computeStats(self):
  sumVal=0;maxVal=-999999;minVal=999999
  for p in self.data:
   val=p[1]
   if val>maxVal:maxVal=val
   if val<minVal:minVal=val
   sumVal+=val
  avg=sumVal/len(self.data)
  return {"avg":avg,"max":maxVal,"min":minVal}

 def checkThreshold(self):
  stats=self.computeStats()
  if stats["avg"]>self.threshold:
   print("Average exceeds threshold!")
  else:
   print("Average within limits.")

def helper_function(a,b,c= []):
    if a> b:
     return[a-b , math.sqrt(a)]
    else:
         for i in range(5): c.append(i*i)
         return c

def main():
 print("Starting Analysis Script")
 scaled,tot=ProcessData(DATA_POINTS,ScaleFactor=2,verbose=True)
 A=analyzer("TestAnalyzer",threshold=20,data=scaled)
 A.checkThreshold()
 stats=A.computeStats()
 print("Stats are:",stats)
 extra=helper_function(10,5)
 print("Extra:",extra)
 if len(sys.argv)>1:
  print("Arguments detected:",sys.argv)

if __name__=="__main__":
    main()

