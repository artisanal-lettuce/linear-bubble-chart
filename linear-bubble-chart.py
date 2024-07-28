#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


# In[2]:


## VARIABLES
input_table = "./test2.csv" # table w/ data
image_name = "./image.png" # name for the saved image
# graph titles and names
graph_title = "this is the title of the graph"
x_axis_title = "this is the title of the x axis"
y_axis_title = "this is the title of the y axis"
x_name = "X name"
y_name = "Y name"


# In[3]:


df = pd.read_csv(input_table)


# In[4]:


size = np.array(df['size'], dtype=np.float32)

fig = px.scatter(df, x='x', y='y',
                 color = 'y',
                 size='size',
                 width=1400,
                 color_discrete_sequence=px.colors.qualitative.Prism, ## more colours https://plotly.com/python/discrete-color/
                 labels={
                     'x' : x_name,
                     'y' : y_name,
                 }
                )

fig.update_layout(
    title=graph_title,
    xaxis=dict(
        title=x_axis_title,
        dtick=3,
    ),
    yaxis=dict(
        title=y_axis_title,
        dtick=1,
    ),
)

fig.show()
fig.write_image(image_name)

