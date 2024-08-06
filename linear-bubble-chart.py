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
image_name = "./image.pdf" # name of the saved image
# graph titles and names
graph_title = "</b>Lipid species altered in NDUFS4 KO cells</b>"
x_axis_title = "Log2 (fold-change of lipid levels)"
y_axis_title = ""
x_name = "Fold change"
y_name = ""
background_color = 'white'  # define background color

# In[3]:

# Read the data

df = pd.read_csv(input_table, sep=';', decimal=",")


# In[4]:

# Convert 'size' column to float32

size = np.array(df['size'], dtype=np.float32)

# Create scatter plot

fig = px.scatter(df, x='x', y='y',
                 color = 'y',
                 size='size',
                 width=1000,
                 height=1000,
                 color_discrete_sequence=px.colors.qualitative.Prism, ## more colours https://plotly.com/python/discrete-color/
                 labels={
                     'x' : x_name,
                     'y' : y_name,
                 }
                )

# Update layout

fig.update_layout(
    title={
        'text': graph_title,
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 28,  # Title font size
            'color': 'Black',  # Title font color
        }
    },
    xaxis=dict(
        title={
            'text': x_axis_title,
            'standoff': 15,  # Adjust the distance of the title from the axis
            'font': {
                'size': 18,  # X-axis title font size
                'color': 'Black',  # X-axis title font color
            }
        },
        dtick=2,
        range=[-1.2, 1.4],  # Set the range for the x-axis
        automargin=True,
        zeroline=False,  # Ensure no zero line is drawn
        showline=True,  # Show x-axis line
        linecolor='black',  # Color of the x-axis line
        linewidth=2,  # Width of the x-axis line
        tickfont={
            'size': 16,  # X-axis tick labels font size
            'color': 'black'  # X-axis tick labels font color
        }
        
    ),
    yaxis=dict(
        title={
            'text': y_axis_title,
            'standoff': 15,  # Adjust the distance of the title from the axis
            'font': {
                'size': 20,  # Y-axis title font size
                'color': 'Black'  # Y-axis title font color
            }
        },
        dtick=1,
        automargin=True,
        zeroline=False,  # Ensure no zero line is drawn
        showline=True,  # Show y-axis line
        linecolor='black',  # Color of the y-axis line
        linewidth=2,  # Width of the y-axis line
        showticklabels=True,  # Set to False to hide y-axis tick labels
        tickfont={
            'size': 18,  # Y-axis tick labels font size
            'color': 'black'  # Y-axis tick labels font color
            }
    ),
    
    plot_bgcolor='white',  # Set the background color of the plotting area
    paper_bgcolor='white',  # Set the background color of the entire figure
    margin=dict(t=120),  # Adjust the top margin to move the title
    showlegend=False  # Hide the legend

)

# Add a semi-transparent vertical line at x=0
fig.add_shape(
    type="line",
    x0=0, x1=0,
    y0=0, y1=1,
    xref="x",
    yref="paper",
    line=dict(color="LightGrey", width=2, dash="dash")


)
   

fig.show()
fig.write_image(image_name)
