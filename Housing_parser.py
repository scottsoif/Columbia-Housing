import csv


def load_doc():
    with open('housing 2020.csv', newline='') as csvfile:  # csv filename goes here
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if not row[2]=='':
                housing.append([float(row[1]),int(row[2]), int(row[4])])

                
def getCol(arr, idx): # returns one-dim array of any column
                      # used below to find index row of your group
    return [i[idx] for i in arr]


def getHousStats(eight=True, nine=False, ten=False, points=20):
    # usage: getHousStats() will return groups of 8 members before you
    #        getHousStats(0,1,1, 20) returns groups of 9 or 10 members
    #        getHousStats(0,1,0, 20) groups with only 9 members and so on
    #        points variable shows only groups >= to that value
    tally = 0;
    for g in housing[:h_idx]:  # g stands for group
        if g[0]>=points and (g[1]==8 and eight) or (g[1]==9 and nine) or (g[1]==10 and ten):
            print(g)
            tally+=1
    print("\n{}  groups before you".format(tally) )

    

if __name__ == '__main__':
    housing = []
    load_doc()
    housing_number = 2266   # input your housing number
    h_idx = getCol(housing, 2).index(housing_number)  # our housing number index

    getHousStats(1,0,0,30)  # same as getHousStats()


