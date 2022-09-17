import json


def CreateData(var, value):
    
    with open("envData.json") as file:
        oldData = json.load(file)
    
    oldData[var] = value
    oldData = json.dumps(oldData, indent=4)

    with open("envData.json", "w") as file:
        file.write(oldData)

