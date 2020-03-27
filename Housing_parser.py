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
h_idx = getCol(housing, 2).index(housing_number)  # our housing number index

def getHousStats(eight=True, nine=False, ten=False):
    # usage: getHousStats() will return groups of 8 members before you
    #        getHousStats(0,1,1) returns groups of 9 or 10 members
    #        getHousStats(0,1,0) groups with only 9 members and so on
    tally = 0;
    for g in housing[:h_idx]:  # g stands for group
        if (g[1]==8 and eight) or (g[1]==9 and nine) or (g[1]==10 and ten):
            print(g)
            tally+=1
    print("\n{}  groups before you".format(tally) )

    
getHousStats() 


