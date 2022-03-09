import pandas as p
import plotly.figure_factory as pf

data = p.read_csv("projectdata.csv")

fig = pf.create_distplot([data["Avg Rating"].tolist()], ["Avg Rating"], show_hist = False)
fig.show() 