import sys
import re
from sklearn import svm
from svmutil import *


files = 7

write_fileX = open('X.txt' , 'w')
write_fileY = open('Y.txt' , 'w')
write_fileXT = open('XT.txt' , 'w')
write_fileYT = open('YT.txt' , 'w')

f = []
for i in range(files):
    f.append(open(str(i)+'.txt', 'r'))

attrbutes = []
y = []

date_dict = []
for i in range(files):
    date_dict.append({})

date_list = []

for i in range(files):
    d = True
    for line in f[i]:
        s = line.split()
        if d == True:
            d = False;
            date = s[0]
            if i == 4:
                date_list.append(date)
        else:
            date_dict[i][date] = float(s[0])
            d = True;

zero_counter = 0
zero_dates = {}

Y = []
X = []

positives = 0
negatives = 0


for date in date_list:
    day_attr = []
    day_string = ''
    zero_entry = []
    for i in range(files):
        if date in date_dict[i]:
            value = date_dict[i][date]
            if i == 4:
                if value >= 0:
                    Y.append(1)
                    positives = positives + 1
                else:
                    Y.append(-1)
                    negatives = negatives + 1
            else:
                day_string = day_string + str(value) + '  '
                day_attr.append(value)
        else:
            zero_counter = zero_counter + 1;
            zero_entry.append(i)
            day_string = day_string + str(0) + '  '
            day_attr.append(0)
        if zero_entry != []:
            zero_dates[date] = zero_entry
    X.append(day_attr)

num_data_points = len(X)

# taking first 15% as test
runs = 0;
end = 0;

while runs < 3:
    runs = runs + 1
    end = end - 0.05;
    num_test = int(0.15*num_data_points)

    end_point  = int((end + 0.95) * num_data_points)

    print "changinf end point"
    print end_point

    X_test = X[0:num_test]
    X_train = X[num_test:end_point]
    Y_test = Y[0:num_test]
    Y_train = Y[num_test:end_point]

    variations = []
    for ind in range(6):
        variations.append(0);

    print len(Y)

    print len(X)

    ind = -1;
    for x in X:
        ind = ind + 1
        for i in range(len(x)):
            if x[i] >= 0:
                if Y[ind] > 0:
                    variations[i] = variations[i] + 1
                else:
                    variations[i] = variations[i] - 0
            else:
                if Y[ind] > 0:
                    variations[i] = variations[i] - 0
                else:
                    variations[i] = variations[i] + 1



    print variations

    print len(Y)

    print len(X)

    for t in X_test:
        s = ''
        for el in t:
            s = s + str(el) + ' '
        write_fileXT.write(s + '\n')

    for t in X_train:
        s = ''
        for el in t:
            s = s + str(el) + ' '
        write_fileX.write(s + '\n')


    for t in Y_test:
        write_fileYT.write(str(t) + '\n')

    for t in Y_train:
        write_fileY.write(str(t) + '\n')

    print "Done writing"
#    write_fileX.close()
#    write_fileY.close()
#    write_fileXT.close()
#    write_fileYT.close()

#sys.exit(0)

    clf = svm.SVC()

    clf.fit(X_train, Y_train)


    print clf.predict(X_test)

    print Y_test

    prob = svm_problem(Y_train,X_train)
    param = svm_parameter('-t 0 -c 4 -b 1 -h 0')

    m = svm_train(prob, param)

    print svm_predict(Y_test ,X_test, m)


    print positives

    print negatives
