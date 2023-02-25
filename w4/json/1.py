import json

with open('sample_data.json') as temp:
    data = json.load(temp)

print("Interface Status")
print("="*80)
print("DN" + " "*49 + "Description" + " "*10 + "MTU Speed")
print("-"*50 + " " + "-"*20 + " " + "-"*5 + " " + "-"*6)

for j in range(0,17):
    for i, k in data["imdata"][j]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="     "*6) 
            print(" ", end="")
        if i == "speed":
            print(k, end=" ")
        if i == "mtu":
            print(k, end="    ")
    print()