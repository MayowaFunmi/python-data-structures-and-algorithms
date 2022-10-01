import random
# user defined functions
def fetchColor(x):  # function to take the randomly generated number, match it with color scheme and return the color based on the scheme
    if x <= 10 and x >= 1:
        temp_color = 'Red'
    if x <= 20 and x >= 11:
        temp_color = 'Green'
    if x <= 30 and x >= 21:
        temp_color = 'Blue'
    if x <= 40 and x >= 31:
        temp_color = 'Purple'
    if x <= 50 and x >= 41:
        temp_color = 'Yellow'
    if x <= 60 and x >= 51:
        temp_color = 'White'
    if x <= 70 and x >= 61:
        temp_color = 'Orange'
    if x <= 80 and x >= 71:
        temp_color = 'Brown'
    if x <= 90 and x >= 81:
        temp_color = 'Black'
    return temp_color
def displayInfo():
    print()
    print("Please enter color: Red, Green, Blue, Purple, Yellow, Black, White, Orange, Brown: ")
    print()
pre_def_colors = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Black', 'White', 'Orange', 'Brown']
# System Part
colors = ['', '', '', '']   # array to store system chosen color
position = 0
num_guess = 0
for i in range(4):
    temp_color = ''
    temp_int = random.randint(1, 90)    # generate random integer
    color = fetchColor(temp_int)    # fetch the color from the predefined scheme in the function
    colors[position] = color    # add generated color to color array
    position += 1
#print(colors)   # uncomment this line
# User part
user_colors = ['', '', '', '']
displayInfo()
while user_colors != colors:
    user_colors = ['', '', '', '']  # clear all  user previously chosen colors
    position2 = 0
    loop = 0
    while loop < 4: # this loop ensures user added 4 correct colors
        usr_color = input("Guess the color: ")  #input color from user
        usr_color = usr_color.capitalize()
        if (usr_color in pre_def_colors):
            user_colors[position2] = usr_color  # saving user color into a separate array
            position2 += 1
            loop += 1
        else:
            print("Color ", usr_color, " is a wrong guess!!. \n choose another color...")
            continue
    print()
    print()
    # Result engine
    user_c = 0
    for c in range(4):
        if (user_colors[user_c] == colors[user_c]):
            print("Color " + user_colors[user_c] + " and its position are correct: ")
            user_c += 1
        elif (user_colors[user_c] in colors and user_colors[user_c] != colors[user_c]):
            print("Color " + user_colors[user_c] + " is correct but position is wrong!")
            user_c += 1
        elif (user_colors[user_c] in colors and user_colors[user_c] == colors[user_c]):
            print("Color and position are correct: ", user_colors[user_c])
            user_c += 1
        else:
            print("Color ", user_colors[user_c], " and Position are incorrcet!!!")
            user_c += 1
    print()
    print()
    num_guess += 1
    print()
print()
print("Number of guess for you to win = ", num_guess)
print(colors)