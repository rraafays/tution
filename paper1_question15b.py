km = int(input("km: "))
fuel = 0
if km > 0:
    fuel = km * 100
    if fuel < 1500:
        fuel = 0
print(str(fuel) + "L")
