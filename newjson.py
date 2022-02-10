import json



fo=open(myjson.json, r)

########### to read or get output

print(json.load(fo))

fo.close()


######## to insert data

my_dict {1:'one',2:'two'}

json.dump(my_dict,fo
