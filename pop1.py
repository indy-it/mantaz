import os

path = "/Users/dani/Documents/MATLAB/Csv-paper/Results1/"
name = 'results_csv_'
name2 = 'results_csv_last_5000_'

f = open('entire_history_pop1.txt', 'w+')
f2 = open('last_5000_history_pop1.txt', 'w+')

onlyfiles = next(os.walk(path))[2]  # dir is your directory path as string
num_csv = int((len(onlyfiles) - 1) / 2)
print('num_csv = ', num_csv)

for i in range(0, num_csv):
    s = open(path + name + str(i + 1) + '.txt')
    s2 = open(path + name2 + str(i + 1) + '.txt')
    a = s.readline()
    b = s2.readline()

    f.write(a + '\n')
    f2.write(b + '\n')

f.close()
f2.close()
