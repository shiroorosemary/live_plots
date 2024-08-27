import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

file_path1 = r"C:\Users\Lenovo X260\Documents\ARC Farmer Adoption.csv"  
df1 = pd.read_csv(file_path1)
file_path2 = r"C:\Users\Lenovo X260\Documents\ARC Farmer Experience.csv"  
df2 = pd.read_csv(file_path2)

for col in ['Edwin', 'Ian', 'Joy']:
    df1[col] = pd.to_numeric(df1[col], errors='coerce') * 100 
    df2[col] = pd.to_numeric(df2[col], errors='coerce') * 100 

fig = make_subplots(
    rows=2, cols=1, 
    subplot_titles=('Farmer Adoption', 'Farmer Experience'),
    vertical_spacing=0.3,  
    row_heights=[0.5, 0.5]  
)

fig.add_trace(go.Scatter(x=df1['Date'], y=df1['Edwin'], mode='lines+markers', name='Edwin'),
              row=1, col=1)
fig.add_trace(go.Scatter(x=df1['Date'], y=df1['Ian'], mode='lines+markers', name='Ian'),
              row=1, col=1)
fig.add_trace(go.Scatter(x=df1['Date'], y=df1['Joy'], mode='lines+markers', name='Joy'),
              row=1, col=1)

fig.add_trace(go.Scatter(x=df2['Date'], y=df2['Edwin'], mode='lines+markers', name='Edwin'),
              row=2, col=1)
fig.add_trace(go.Scatter(x=df2['Date'], y=df2['Ian'], mode='lines+markers', name='Ian'),
              row=2, col=1)
fig.add_trace(go.Scatter(x=df2['Date'], y=df2['Joy'], mode='lines+markers', name='Joy'),
              row=2, col=1)

global_min = min(df1[['Edwin', 'Ian', 'Joy']].min().min(), df2[['Edwin', 'Ian', 'Joy']].min().min())
global_max = max(df1[['Edwin', 'Ian', 'Joy']].max().max(), df2[['Edwin', 'Ian', 'Joy']].max().max())

# Update y-axes
fig.update_yaxes(title_text='Percentage (%)', range=[global_min, global_max], row=1, col=1)
fig.update_yaxes(title_text='Percentage (%)', range=[global_min, global_max], row=2, col=1)
fig.update_yaxes(tickformat=".0f%%", row=1, col=1)
fig.update_yaxes(tickformat=".0f%%", row=2, col=1)


fig.update_layout(
    title_text='ARC REPORT GRAPHS',
    showlegend=True,
    height=800, 
    width=1200   
)

st.plotly_chart(fig)
