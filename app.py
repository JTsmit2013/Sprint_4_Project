import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Raw Vehicle Data')
st.dataframe(df)

# -------------------------------------------------------
st.header('Vehicle types by manufacturer')
st.write(px.histogram(df, x='manufacturer', color='type'))

# -------------------------------------------------------
st.header('Histogram of `condition` vs `model_year`')
st.write(px.histogram(df, x='model_year', color='condition'))
          
# -------------------------------------------------------
st.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox('Select manufacturer 1',
                              manufac_list, index=manufac_list.index('chevrolet'))

manufacturer_2 = st.selectbox('Select manufacturer 2',
                              manufac_list, index=manufac_list.index('hyundai'))
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay'))

# -------------------------------------------------------
st.title('Scatter Plot by Manufacturer')

# Sidebar filters
manufacturers = df['manufacturer'].unique()
selected_manufacturers = st.multiselect('Select Manufacturers', manufacturers, default=manufacturers)

min_price = int(df['price'].min())
max_price = int(df['price'].max())
price_range = st.slider('Select Price Range', min_price, max_price, (min_price, max_price))

min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())
year_range = st.slider('Select Model Year Range', min_year, max_year, (min_year, max_year))

# Filter data
filtered_df = df[
    (df['manufacturer'].isin(selected_manufacturers)) &
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['model_year'] >= year_range[0]) &
    (df['model_year'] <= year_range[1])
]

# Create the plot
fig = go.Figure()
colors = px.colors.qualitative.Safe

for i, manufacturer in enumerate(selected_manufacturers):
    df_filtered = filtered_df[filtered_df['manufacturer'] == manufacturer]
    fig.add_trace(go.Scatter(
        x=df_filtered['model_year'],
        y=df_filtered['price'],
        mode='markers',
        name=manufacturer,
        marker=dict(color=colors[i % len(colors)])  # Ensure distinct colors using modulo
    ))

# Update layout
fig.update_layout(
    title='Scatter Plot by Manufacturer',
    xaxis_title='Model Year',
    yaxis_title='Price',
    height=600
)

# Show plot in Streamlit
st.plotly_chart(fig)
