import csv 
from csv import reader
from re import L
import time as time
import numpy as np
# import matplotlib.pyplot as plt

Time_to_Read_from_file=0
Time_to_calculate_from_Point = 0
Time_to_sort_lists = 0
algorithm :str

#insertion sort of tuple list 
def insertionSort(arr, key=lambda x: x):
    for index in range(1, len(arr)):
        currentvalue = arr[index]
        position = index
        while position > 0 and key(arr[position - 1]) > key(currentvalue):
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = currentvalue
    # print( "Sorted : " + str(arr))
    return arr[0][0]

#tuple list for bubbleSort
def bubbleSort(arr): 
    ith = 1
    list_length = len(arr)  
    for i in range(0, list_length):  
        for j in range(0, list_length-i-1):  
            if (arr[j][ith] > arr[j + 1][ith]):  
                temp = arr[j]  
                arr[j]= arr[j + 1]  
                arr[j + 1]= temp 
    # print( "Sorted : " + str(arr))
    return arr[0][0]

#tuple list for merge sort
def mergeSort(arr, key=lambda x: x):
    if len(arr) < 2:
        return arr[0][0]

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left , key=lambda x:(x[1], int(x[0][0]) , int(x[0][1])))
    mergeSort(right, key=lambda x:(x[1], int(x[0][0]) , int(x[0][1])))

    i = j = k = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    # print(arr , arr[0][0])
    return arr[0][0]

#tuple list for Partition Quick
def partition(arr, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1)
  
 
#tuple list for Quick Sort
def quickSort(arr , low, high ): 
    if len(arr) == 1: 
        print( "Ster" , arr[0][0])
        return arr[0][0]
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
        print(pi)
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# quick sort 2
def quicksort(arr , key=lambda x:x):
  if len(arr) <= 1:
    return arr

  left  = []
  right = []
  equal = []
  pivot = arr[0]
  for num in arr:
    if num < pivot:
      left.append(num)
    elif num == pivot:
      equal.append(num)
    else:
      right.append(num)
  
  arr.append(quicksort(left , key=lambda x:x[1]))
  arr.append(equal)
  arr.append(quicksort(right, key=lambda x:x[1]))
  print(arr)
#TO make Undirected File
def UnDirected_graph(lists):
    output, seen = [], set()
    for item in lists:
        t1 = tuple(item)
        if t1 not in seen and tuple(reversed(item)) not in seen:
            seen.add(t1)
            output.append(item)

    return output

# make the graph with read from txt file 
def make_graph(fileName):
    vertices = []
    global Time_to_Read_from_file 
    before= time.time()
    with open(fileName) as infile:
        for line in infile:
            line = line.strip()
            words = line.split('\t')
            vertex = (words[0] , words[1])
            vertices.append(vertex)
    after =time.time()
    Time_to_Read_from_file = round(after-before , 5)
    print("Time_to_Read_from_file" ,  Time_to_Read_from_file)
    vertices = UnDirected_graph(vertices)
    return vertices

# determine the Degree of the each node    
def degree(vertices , A , B):
    Ki = 0
    Kj = 0
    for x in vertices:
        if (x[0]==A or x[1]==A):
            Ki = Ki +1 
        if (x[0]==B or x[1]==B):
            Kj = Kj +1
    return Ki-1 , Kj-1

# determine point to the vertex 
def point_to_vertex(vertices , Sort_Type):
    Ki = 0 
    Kj = 0
    Zij = 0
    count = 1
    global Time_to_calculate_from_Point 
    global Time_to_sort_lists 
    # Time_to_calculate_from_Point = 0
    # Time_to_sort_lists = 0
    while(check_connected(vertices)):
        dictionary = dict()
        Zij = 0
        Ki = 0 
        Kj = 0
        before1 = time.time()
        for A in vertices:
            Zij = 0
            Ki = 0 
            Kj = 0
            for B in vertices:
                if(A[0] == B[0] or A[0] == B[1]):
                    Ki = Ki+1
                if(A[1] == B[0] or A[1] == B[1]):
                    Kj = Kj+1
                for C in vertices:
                    if A[1] == B[0] and B[1] == C[0] :
                        Zij = Zij + 1
            # print(A , Ki , Kj , Zij)
            if(Ki == 1  or Kj == 1):
                dictionary[A] = 1000000000
            else:
                dictionary[A] = (Zij+1) / (min(Ki-1  , Kj-1 ))
        after1 =time.time()
        Time_to_calculate_from_Point = Time_to_calculate_from_Point + round(after1 - before1 , 5)
        lists = []
        for key , value in dictionary.items() :
            x = (key , value)
            lists.append(x)
        before = time.time()
        if(Sort_Type == "Bubble"):
            vertices = delete_vertex(vertices , bubbleSort(lists))
        if(Sort_Type == "Quick"):
            n = len(lists)
            # quickSort(lists , 0 , n-1)
            # quicksort(lists ,  key=lambda x:x[1])
            # vertices = delete_vertex(vertices , quickSort(lists , 0 , n-1 , key=lambda x:x[1]))
        if(Sort_Type == "Merge"):
            vertices = delete_vertex(vertices , mergeSort(lists , key=lambda x:(x[1], int(x[0][0]) , int(x[0][1]))))
        if(Sort_Type == "Insertion"):
            vertices = delete_vertex(vertices , insertionSort(lists , key=lambda x:x[1]))
        else:
            print("NO Sort Algorithm Find")
            return False
        after = time.time()
        Time_to_sort_lists = Time_to_sort_lists + round(after - before , 5)
        count = count - 1
    print(vertices)

# Check if the Graph is connected 
def check_connected(vertices):
    A = []
    B = []
    for graph in vertices:
        if(len(A) == 0):
            A.append(graph[0])
            A.append(graph[1])
        elif(graph[0] in A):
            if(graph[1] in A):
                continue
            elif(graph[1] not in B):
                A.append(graph[1])
            elif(graph[1] in B):
                # print(A , B)
                return True
        elif(graph[1] in A ):
            if(graph[0] in A):
                continue
            if(graph[0] not in B):
                A.append(graph[0])
            elif(graph[0] in B):
                # print(A , B)
                return True
        
        elif(len(B) == 0):
            B.append(graph[0])
            B.append(graph[1])
        
        elif(graph[0] in B):
            if(graph[1] in B):
                continue
            elif(graph[1] not in A):
                B.append(graph[1])
            elif(graph[1] in A):
                # print(A , B)
                return True
        
        elif(graph[1] in B):
            if(graph[0] in B):
                continue
            if(graph[0] not in A):
                B.append(graph[0])
            elif(graph[0] in A):
                # print(A , B)
                return True
        
        else:
            # print(A , B)
            A.append(graph[0])
            A.append(graph[1])           
    
    if(len(B) == 0):
        return True
    print(A , B , len(A) + len(B))
    write_to_csv(A , B)
    return False

# delete the vertex from lists 
def delete_vertex(lists:list , key):
    lists.remove(key)
    return lists

# make the csv file 
def to_csv(fileName):
    file = open(fileName , mode='r')
    data = []
    for line in file:
        x , y = line.split('\t')
        data.append([int(x) , int(y)])
    file.close()
    with open('csv' +fileName.split('.')[0] + '.csv' , 'w' , newline='') as file:
        writer = csv.writer (file)
        writer.writerows(data)

# read the csv file and make the list of tuple
def read_csv(fileName):
    global Time_to_Read_from_file 
    before= time.time()
    with open(fileName , 'r' ) as read_tuple:
        csv_reader = reader(read_tuple)
        list_of_rows = list(map(tuple ,  csv_reader))
        # print(list_of_rows , list_of_rows[1][1])
    after =time.time()
    Time_to_Read_from_file = round(after-before , 5)
    print("Time_to_Read_from_file" ,  Time_to_Read_from_file)
    vertices = UnDirected_graph(list_of_rows)
    return vertices

# write in csv file
def write_to_csv(A , B):
    global Time_to_calculate_from_Point
    global Time_to_Read_from_file
    global Time_to_sort_lists
    with open('A&B-Bubble-txt.csv', 'w') as csvfile:
        csvfile.write(str(Time_to_Read_from_file) + "\t Time to read from File" + '\n')
        csvfile.write(str(Time_to_calculate_from_Point) + "\t Time to Calculate Point" + '\n')
        csvfile.write(str(Time_to_sort_lists) + "\t Time To sort Lists" + '\n')
        for index in A:
            csvfile.write(index + "A" + '\n')
        for index in B:
            csvfile.write(index + "B" + '\n')
        print(Time_to_Read_from_file , Time_to_calculate_from_Point , Time_to_sort_lists , A ,B)
        

# make_graph()
# to_csv("./test12.txt")
type_of_sort = input()

before = time.time()
# read from TXT file 
point_to_vertex(make_graph("test13.txt") , type_of_sort)
# read from CSV File
# point_to_vertex(read_csv("./Book.csv") , "Insertion")
after = time.time()

print(f"computing scores for first time: {round(after - before , 5)} seconds")