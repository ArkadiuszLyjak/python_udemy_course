# def createUser(name, contact):
#     user = {
#         "name": name,
#         "email": None,
#         "telephone": None
#     }
#
#     if isinstance(contact, str):
#         user["email"] = contact
#     elif isinstance(contact, int):
#         user["telephone"] = contact
#
#     return user
#
#
# user = createUser("Arek", "arek@wp.pl")
# print(user)

def displayShoppingList(shopping_list):
    print("to jest lista zakupowa")
    for item in shopping_list:
        print(" - " + item)


shoppingList = []

while True:
    product = input("Podaj produkt: ")
    if product == "exit": break
    shoppingList.append(product)

displayShoppingList(shoppingList)
