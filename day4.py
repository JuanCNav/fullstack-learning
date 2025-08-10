fruits = ["apple", "banana", "cherry"]
fruits.append("apple")
for fruit in fruits:
    print(f"I like {fruit}")

print(len(fruits))
print(fruits[2])



juan={"name":"Juan Navarro", "height":"6`3", "nationality":"Colombian"}
print(juan["name"])
print(juan["nationality"])

for key, value in juan.items():
    print(f"{key} → {value}")