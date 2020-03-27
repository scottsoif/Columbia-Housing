import csv

housing = []

def load_doc():
    with open('housing 2020.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if not row[2]=='':
                housing.append([float(row[1]),int(row[2]), int(row[4])])

                
def getCol(arr, idx):
    return [i[idx] for i in arr]

load_doc()
housing_number = 2266   # input your housing number
h_idx = getCol(housing, 2).index(housing_number)  # our housing number

def getHousStats():
    tally = 0;
    for row in housing[:h_idx]:
        if row[0] <= 30 and row[1]>=8:
            print(row)
            tally+=1
    print(tally)
    
tally = 0;
for row in housing[:h_idx]:
    if row[0] <= 30 and row[1]>=8:
        print(row)
        tally+=1          
print(tally)


