bikes = ["ktm", "royal enfield", "hardly davidson", "kawasaki", "yamaha"]

if "ktm" in bikes:
    print("ktm exists")
if "ktm" not in bikes:
    print("Ktms doesnot exists")

"""
i = 0
while i < len(bikes):
    print(bikes[i])
    i += 1

for i in range(len(bikes)):
    print(bikes[i])
"""

for bike in bikes:
    print(bike)

