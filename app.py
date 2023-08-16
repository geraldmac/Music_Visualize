# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('music_project_en (1).csv')
# Set page title and options
st.title('Music Data Visualization')
st.header('Music Dataset')
df['Count'] = df.index+1
# Reorder the columns to place 'Count' at the first position
new_column_order = ['Count'] + [col for col in df.columns if col != 'Count']
df = df[new_column_order]

st.write(df)




top_ten_artist = df['artist'].sort_values(ascending=False).head(20)
data_filtered = df[df['artist'].isin(top_ten_artist)]
# Filter out rows with empty artist values
data_filtered = data_filtered[data_filtered['artist'] != ' ']

st.header('Top 10 Artists')

st.write(data_filtered)



# Create checkbox for plot type
use_scatter_plot = st.checkbox('Use Scatter Plot', value=True)

# Create checkbox for plot type
use_hist_plot = st.checkbox('Use Histogram Plot', value=True)

# Create dropdown for feature selection
selected_feature = st.selectbox('Select Feature', df.columns)

if use_hist_plot:
    fig = px.histogram(df, x=selected_feature, title=f'Histogram of {selected_feature}')
    fig.update_layout(height=1000,width=1000)

    st.plotly_chart(fig)

# Create scatter plot or histogram based on user selection
st.header(f'Visualization of {selected_feature}')

if use_scatter_plot:
    x_axis = st.selectbox('Select X-Axis Feature', df.columns)
    y_axis = st.selectbox('Select Y-Axis Feature', df.columns)

    # Create checkbox for using color
    use_color = st.checkbox('Use Color', value=True)
    if use_color:
        color = st.selectbox('With Respect to/ Color', df.columns)
    
        fig = px.scatter(df, x=x_axis, y=y_axis,color=color, title=f'Scatter Plot: {x_axis} vs {y_axis}',range_x=[30,70000])
        # Increase scatter plot height and width
        fig.update_layout(width=1000,height=1000)
    else:
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot: {x_axis} vs {y_axis}',range_x=[30,70000])
        # Increase scatter plot height and width
        fig.update_layout(width=1000,height=1000)    

    st.plotly_chart(fig)





