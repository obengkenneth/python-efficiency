# using the filter function

temps = [12.5, 13.6, 15, 9.2]
filtered_temps = list(filter(lambda a: True if (9/5) * a + 32 > 55 else False, temps)) 
print(filtered_temps)