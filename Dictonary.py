empt_dict = {}

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2026,
    "spec": {
        "height": "26",
        "weight": "900kg",
        "mileage": "20km"
    },
    "num": [10,20,30]
}

print(car["brand"])
# print(car["released"])
print(car.get("released", 0))

spec = car.get("spec")
print(spec)

car["model"] = "F-150"
print(car)

car["price"] = "500000"
print(car)

car.update({
    "model": "mustang",
    "price": 600000
})

print(car)

del car["price"]
print(car)
# car.clear()

print(car.keys())
print(car.values())

if "model" in car:
    print("the key exist")

if "price" not in car:
    print("Key price doesn't exist")    