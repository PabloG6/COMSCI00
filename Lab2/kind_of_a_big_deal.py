minutes = float(input("Minutes: "))
num_hours = minutes//60
num_minutes = minutes%60
num_seconds = 60*(num_minutes%1)

print(int(num_hours), "hours", int(num_minutes), "minutes", int(num_seconds), "seconds")

