import json
#from collections import OrderedDict
#response.encoding = 'utf-8' 

g = open('ptt_0726_s.json', 'r',encoding ='utf-8')
data=json.load(g)



for i in range (0,len(data)):
    
    #print(data[i]['h_推文總數'])
    if len(data[i]['h_推文總數'])==0:
        data[i]['h_推文總數']['all']=0
answer=sorted(data,key=lambda x:x['h_推文總數']['all'],reverse=True)

#print(answer)


print(json.dumps(answer, indent=5,ensure_ascii=False))
#b=sorted(final[i]['h_推文總數'])
    
#print(data[0]['h_推文總數']['all'])
#print(data[1]['h_推文總數']['all'])
#print(data[2]['h_推文總數'])