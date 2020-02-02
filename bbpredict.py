from sklearn import tree
import pandas as pd
import sys
import unittest
import csv
'''
For more advanced models, lookup hitter ID
and their respective tendencies
and location.
'''

try:
    f=open(sys.argv[1])
    reader = csv.DictReader(f,delimiter=',')
    team=input("Name the Pitcher's Team Acronym (NYM,ATL,etc)")
except:
    print("File Not Existent")
    sys.exit(1)

try:
    writecsv=open("output.csv",'w')
    writecsv.write("Count,Ahead,Close,AfterFifth,Righty,Pitch\n")
    '''
    Format Data for Actual Predictions
    '''
    for i in reader:
        if(team==i['home_team']):
            home=True
        elif(team==i['away_team']):
            home=False
        else:
            print("Incorrect Team Acronym.")
            f.close()
            writecsv.close()
            sys.exit(1)
        count=str(i['balls'])+"-"+str(i['strikes'])
        x=int(i['home_score'])
        y=int(i['away_score'])
        if(home):
            ahead=x-y>0
        else:
            ahead=x-y<0
        close=abs(x-y)<3
        AfterFifth=int(i['inning'])>5
        Righty='R'==i['stand']
        pitchtype=i['pitch_name']

        writecsv.write(count+","+str(ahead)+","+ str(close)+","+str(AfterFifth)+","+str(Righty)+","+pitchtype+"\n")
    writecsv.close()
    df=pd.read_csv("output.csv")
    print(df)

except:
    print("Incorrect File Format")
    f.close()
    sys.exit(1)
