train = open("ad_train.csv", "r")
train_sampled = open("ad_train_sampled.csv", "w")

cont = 0
cont_not_null = 0
x = 0
y = 0
z = 0
heart = 0
for line in train:
    cont += 1
    values = line.split(",")
    
    if not int(values[4]) == -1:
        cont_not_null += 1
        x += int(values[1])
        y += int(values[2])
        z += int(values[3])
        heart += int(values[4])

    if cont % 10 == 0:
        if cont_not_null > 0:
            train_sampled.write(str(x / cont_not_null) + "," + str(y / cont_not_null) + "," + str(z / cont_not_null) + "," + str(heart / cont_not_null) + "\n")
        x = 0
        y = 0
        z = 0
        heart = 0
        cont_not_null = 0

train.close()
train_sampled.close()