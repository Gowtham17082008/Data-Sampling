import pandas as pd
import plotly.figure_factory as pf
import statistics 
import random
import plotly.graph_objects as ff
import csv

df=pd.read_csv("data.csv")
data = df["reading_time"].toist()
graph=ff.creat_destplot([data], ["reading_time"], show_hist=False)
graph.show()

population_mean=statistics.mean(data)
print("mean =", population_mean)
population_stdev=statistics.stdev(data)
print("standard Deviation =", population_stdev)

dataset=[]
for i in random (0,100):
    random_index=random.randint(0, len(data))
    valu=data[random_index]
    dataset.append(valu)
    mean=statistics.mean(dataset)
    standreddeviation=statistics.stdev(dataset)
    print("mean of 1000 value", mean)
    print("stdev of 1000 value",statistics.stdev)