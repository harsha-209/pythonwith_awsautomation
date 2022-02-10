import csv


fo = open("/home/minfy/Downloads/logs-insights-results.csv",'r')
content = csv.reader(fo,delimiter="|")

for a in content:
    #print(a)
    if 'load_id' in a:
        print(a)

fo.close()