
import csv


with open("Movies.csv","w",newline='') as f:
    w=csv.writer(f,delimiter=",")
    w.writerow([1,2,3,4,5])
    w.writerow([6,7,8,9,10])
