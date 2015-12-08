accuracy = [i for i in range(100)]

total_time = 345.65

with open('res.txt', 'w') as f:
    for acc in accuracy:
        f.write(str(acc) + "\n")
    t = str(total_time)
    f.write("\n\nTime taken: " + t + " minutes")