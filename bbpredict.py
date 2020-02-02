from sklearn import tree
import pandas as pd
import sys

try:
    f=open(sys.argv[1])
    reader = csv.DictReader(f,delimiter=',')
    team=input("Name the Pitcher's Team Acronym (NYM,ATL,etc)")
except:
    print("File Not Existent")
    sys.exit()

try:
    writecsv=open("output.csv",'w')
    writecsv.write("Count,SecureLead,Ahead,AfterFifth,Pitch\n")
  '''
  Format Data for Actual Predictions
  '''
  for i in reader:

    writecsv.close()
except:
    print("Incorrect Team Name or Incorrect File Format")
    f.close()
