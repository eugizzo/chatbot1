import json

with open('intents.json') as f:
    intents=json.load(f)

tags=[]
for intent in intents['intents']:
    tag=intent['tag']
    tags.append(tag)
    print(tags)
