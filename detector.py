from vanguard.aleo.common import aleo2json

json_obj = aleo2json("./hello/build/main.aleo")

import json 
# with open("./main.json", "r") as f:
#     json_obj = json.load(f)


print(f"json_obj: {json_obj}")
insts = json_obj["functions"]["hello"]["instructions"]
print(insts)
result  =False 
for inst in insts:
    tokens  = inst["str"].strip(";").split()
    print(tokens)
    # match tokens:
    #     case ["div", r0, r1, "into", r3]:
    #         result = True
    #     case _:
    #         pass

    if tokens[0] =="div":
        result = True

print("Result:", result)