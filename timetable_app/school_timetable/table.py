# create grid 
no_of_days = int(input("Enter number of days: "))
no_of_periods = int(input("Enter number of periods: "))

grid = []
for i in range(no_of_days):
    grid.append([i])
    for j in range(no_of_periods):
        grid[i].append(j)
print(grid)