"""
"ravi@gmail.com" -> Ravi Sharma
"priya@gmail.com" -> Priya
"""

users = {}

#insert

users["ravi@gmail.com"] = "Ravi Sharma"
users["priya@gmail.com"] = "Priya"
users["mohak@gmail.com"] = "mohak"

print(users["ravi@gmail.com"])

print("ravi@gmail.com" in users)

users["priya@gmail.com"] = "Priya Sharma"
print(users)

del users["mohak@gmail.com"]
print(users)
print(users.keys)
print(users.values)
print(users.items)