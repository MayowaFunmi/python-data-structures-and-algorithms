import random

Teachers = ['mayowa', 'esther']
Class = [1, 2, 3]
Day = ['monday', 'wednesday', 'friday']
Data = []
Lecture = ['maths', 'english', 'physics', 'chemistry', 'biology']

def index():
    classes = Class
    teachers = Teachers
    day = Day
    data = []

    total_c = len(Class)
    total_d = len(Day)
    total_l = len(Lecture)
    total = total_c * total_d * total_l

    for x in range(total):
        randInddex = random.choice(teachers)
        data.append(randInddex)
    total_t = total_l * total_d
    if (total_c == 3):
        for x in range(0, total_t, 1):
            while (data[x] == data[x + total_t] or data[x] == data[x + total_t * 2]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t, total_t * 2, 1):
            while (data[x] == data[x + total_t]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)

    if (total_c == 4):
        for x in range(0, total_t, 1):
            while (data[x] == data[x + total_t] or data[x] == data[x + total_t * 2]or data[x] == data[x + total_t * 3]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t, total_t*2, 1):
            while (data[x] == data[x + total_t]or data[x] == data[x + total_t*2]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t*2, total_t*3, 1):
            while (data[x] == data[x + total_t]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)

    if (total_c == 5):
        for x in range(0, total_t, 1):
            while (data[x] == data[x + total_t] or data[x] == data[x + total_t * 2]or data[x] == data[x + total_t * 3]or data[x] == data[x + total_t * 4]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t, total_t * 2, 1):
            while (data[x] == data[x + total_t] or data[x] == data[x + total_t * 2]or data[x] == data[x + total_t * 3]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t * 2, total_t * 3, 1):
            while (data[x] == data[x + total_t]or data[x] == data[x + total_t*2]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)
        for x in range(total_t*3, total_t*4, 1):
            while (data[x] == data[x + total_t]):
                randIndex = random.choice(teachers)
                data[x] = (randIndex)


print(index())
