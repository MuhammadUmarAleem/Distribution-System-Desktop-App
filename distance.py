import csv
from classes import MedicalStore,MedicalStoreNode
medicalstores = MedicalStore()
def readmedicalStore():
    try:
            with open("MedicalStore.csv", 'r') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                            if (row[0] != 'StoreName'):
                                    data = MedicalStoreNode(row[3], row[4], row[0],
                                                            row[1], row[2])
                                    data.bill = row[5]
                                    medicalstores.addMedicalStore(data)
    except:
            print("MedicalStore.csv")
    
readmedicalStore()

from geopy.distance import geodesic as GD
from networkx.algorithms import tree
import networkx as nx
# For the specified locations, load their latitude and longitude data.
# Abuja =(9.072264 , 7.491302)
# Dakar =(14.716677 , -17.467686)
s = medicalstores.head
temp = []
# G = nx.Graph()
G = nx.cycle_graph(0)
while s != None:
    temp1 = []
    z = medicalstores.head
    while z != None:
        G.add_edge(s.mName,z.mName,weight=GD((s.lattitude,s.longitude),(z.lattitude,z.longitude)).km)
        temp1.append(GD((s.lattitude,s.longitude),(z.lattitude,z.longitude)).km)
        z = z.next
    temp.append(temp1)
    s = s.next

# print(nx.bf(G,"Muneeb Pharmacy","Shahbaz Pharmacy",weight = 'weight'))
print(G)
mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
edgelist = list(mst)
print(edgelist)
# print(str(sorted(sorted(e) for e in edgelist)))

temp1 = []
def isalreadypresent(i):
    for i in temp1:
        for j in i:
            if i[1] == j:
                return True
    return False

def check(i):
    if isalreadypresent(i) == False:
        for j in edgelist:
            if (i[1] == j[0]):
                x = list(i)
                x.append(j[1])
                temp1.append(tuple(x))
                edgelist.remove(j)
                return 0
        return 1
    else: 
        return 2

def shortestdistance():
    for i in edgelist:
        flag = check(i)
        if flag == 1:
            temp1.append(i)
        elif flag == 2:
            x = []
            x.append(i[0])
            temp1.append(tuple(x))

shortestdistance()
print(temp1)

for i in range(len(temp)):
    print(temp[i])

