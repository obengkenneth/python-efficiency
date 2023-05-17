# map with lambdas
temps = [12.5, 13.6, 15, 9.2]
converted_temps = list(map((lambda c: (9/5) * c + 32), temps))
print(converted_temps)
