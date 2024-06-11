import os
files = os.listdir()
file_data = []
for file in files:
    if file.endswith(".txt"):
        with open(file, 'r', encoding= 'utf-8') as f:
            lines = f.readlines()
            file_data.append((file, len(lines), lines))
file_data.sort(key=lambda x: x[1])
with open("new.txt", 'w', encoding= 'utf-8') as f:
    for data in file_data:
        f.write(data[0] + '\n')
        f.write(str(data[1]) + '\n')
        for line in data[2]:
            f.write(line)
