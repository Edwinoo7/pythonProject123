dict={"Fruit":"mango","Vegetable":"Onion","Bread":"Jam","KG":50}
print(dict)
print(dict["KG"])
print(dict["Fruit"])
print(dict.keys())
print(dict.values())
print(dict.pop("Vegetable"))
print(dict)
dict.update({"Fruit":"Apple"})
print(dict)
dict.update({"Road":"Vechile"})
print(dict)
x=dict.copy()
print(x)
y=dict.keys()
print(y)