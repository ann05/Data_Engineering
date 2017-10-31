import pandas as pd
import numpy as np
import sys


zip_dict = {} #to store all the zip_code based transactions as a dictionary
date_dict = {} #to store all the transaction_dt based transactions as a dictionary
file1 = open(sys.argv[2],"w")
file2 = open(sys.argv[3],"w")
def by_zip():
    #ZIP_CODE should be taken as only the first 5 digits
    zip_5 = str(curr[10])[0:5]
    tup = (curr[0],zip_5)
    amt = int(curr[14])
    if(tup not in zip_dict.keys()):
        zip_dict.setdefault(tup,[])
        temp=[]
        l=[]
        l.append(amt)
        temp.append(l)
        temp.append(1)
        temp.append(amt)
        zip_dict[tup]=(temp)
        #print zip_dict[tup]
        f=(curr[0]+'|'+(zip_5)+'|'+str(temp[0][0])+'|'+str(temp[1])+'|'+str(temp[2])+'\n')
        file1.write(str(f))
    else:
        temp=zip_dict[tup]
        temp[0].append(amt)
        med = int(round(np.median(np.array(temp[0]))))
        temp[1]+=1
        temp[2]+=amt
        zip_dict[tup]=temp
        f=curr[0]+"|"+(zip_5)+'|'+str(med)+'|'+str(temp[1])+'|'+str(temp[2])+'\n'
        file1.write(str((f)))
 
        
def by_date():
    tup = (curr[0],curr[13]) 
    amt = int(curr[14])
    if(tup not in date_dict.keys()):
        date_dict.setdefault(tup,[])
        l=[]
        l.append(amt)
        temp=[]
        temp.append(l)
        temp.append(1)
        temp.append(amt)
        date_dict[tup]=temp
    else:
        temp = date_dict[tup]
        temp[0].append(amt)
        temp[1]+=1
        temp[2]+=amt
        date_dict[tup]=temp
i=0
with open(sys.argv[1], "r") as f:
    while(1):
        line=f.readline()
        if not line:
            break
        else:
            curr=line.split("|")
            #CMTE_ID=0
            #ZIP_CODE=10
            #TRANSACTION_DT=13
            #TRANSACTION_AMT=14
            #OTHER_ID=15
            #print curr[0],curr[10],curr[13],curr[14],curr[15]
            i=i+1
            print(i)
            if(pd.isnull(curr[0]) or pd.isnull(curr[14]) or len(curr[15])>0):
                continue
            if(len(curr[10])>=5):
                by_zip()
            if(len(curr[13])==8):
                by_date()
    
#sorting the dictionary by CMTE_ID and TRANSACTION_DT    
for c_id in sorted(date_dict, key=lambda key:(key[0],key[1])):
    med=int(round(np.median(np.array(date_dict[c_id][0])))) #finding the final median of all the amounts
    file2.write(c_id[0]+"|"+(c_id[1])+"|"+str(med)+"|"+str(date_dict[c_id][1])+'|'+str(date_dict[c_id][2])+'\n')


file2.close()
file1.close()
