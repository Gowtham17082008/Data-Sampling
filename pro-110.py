import pandas as pd
import plotly.figure_factory as pf
import statistics 
import random
import plotly.graph_objects as pg

df=pd.read_csv("ARCHIVE(2)/data.csv")
data=df["temp"].tolist()
mean=statistics.mean(data)
stdev=statistics.stdev(data)
print(mean)
print(stdev)
graph=pf.create_distplot([data],["temp"],show_hist=False)
graph.show()

