# there are 125 hens at the small farm
hens = 125
# each hen lays 7 eggs per day
eggs = 7
# total amount of eggs laid daily (125 * 7)
daily_eggs = hens * eggs
# each carton can hold 6 eggs
# to work out how many cartons sold per day floor divide the daily amount of eggs by 6 (875 // 6)
cartons_sold = daily_eggs // 6
# if the amount of cartons sold daily at the farm is less than 100 then multiply the total amount of cartons by 1.00
if cartons_sold < 100:
    daily_cartons = cartons_sold * 1.00
# otherwise if the amount of cartons sold daily at the farm is more than 150 then multiply the total amount of cartons by 1.10
elif cartons_sold > 150:
    daily_cartons = cartons_sold * 1.10
# otherwise multiply the total amount of cartons by 1.05
else:
    daily_cartons = cartons_sold * 1.05

print ('The value of cartons sold daily at the small farm is £',daily_cartons)
