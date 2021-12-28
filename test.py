import json

x = '{ "name" : "John", "age" : 30, "gender" : "male" }'

y = json.loads(x)

print(y)