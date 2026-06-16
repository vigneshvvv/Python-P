class productInformation:
    id = 0
    productName = ""
    description = ""
    price = 0
    tags = []



product1 = productInformation()
product1.id =1
product1.productName = "mobile"
product1.description = "Electronics"
product1.price = 20000
product1.tags[0] = "new"

name = product1.productName
print(product1.productName)
print(name)

product2 = productInformation()
product2.id =2
product2.productName = "laptop"
product2.description = "Electronics"
product2.price = 40000