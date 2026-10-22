# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np  # For adding jitter

# Load SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Initialize Dash app
app = dash.Dash(__name__)

# Generate dropdown options: 'All Sites' plus unique launch sites
unique_sites = [{'label': 'All Sites', 'value': 'ALL'}]
unique_sites.extend([{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()])

# App layout with dropdown, pie chart, payload slider, and scatter plot
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Launch site selector
    dcc.Dropdown(
        id='site-dropdown',
        options=unique_sites,
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True
    ),
    html.Br(),

    # TASK 2: Pie chart for success counts
    # Shows all sites (total) or selected site (success vs failure)
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Payload range filter
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload],
        marks={i: f'{i}kg' for i in range(0, int(max_payload) + 1, 1000)}
    ),

    # TASK 4: Scatter plot for payload vs success correlation
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Update pie chart based on site selection
@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def update_pie_chart(site_dropdown):
    # Donut chart settings
    HOLE_SIZE = 0.3
    COLOR_MAP = {'Failure': 'red', 'Success': 'blue'}

    if site_dropdown == 'ALL':
        # Show total successful launches per site
        success_df = spacex_df[spacex_df['class'] == 1]
        if success_df.empty:
            fig = px.pie(title='No successful launches found')
            return fig
        fig = px.pie(success_df, names='Launch Site',
                     title='Total Successful Launches by Site',
                     hole=HOLE_SIZE)
    else:
        # Show success vs failure breakdown for selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == site_dropdown]
        if filtered_df.empty:
            fig = px.pie(title=f'No launches found for {site_dropdown}')
            return fig
        
        # Map class values to readable labels
        filtered_df_mapped = filtered_df.copy()
        filtered_df_mapped['Outcome'] = filtered_df_mapped['class'].map(
            {0: 'Failure', 1: 'Success'}
        )
        
        fig = px.pie(
            filtered_df_mapped,
            names='Outcome',
            title=f'Success vs Failed Launches for {site_dropdown}',
            hole=HOLE_SIZE,
            color='Outcome',
            color_discrete_map=COLOR_MAP
        )
        
        fig.update_traces(sort=False)  # Maintain legend order
        
    return fig

# TASK 4: Update scatter plot based on site and payload range
@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'), Input('payload-slider', 'value')])
def update_scatter_chart(site_dropdown, payload_range):
    min_payload_range, max_payload_range = payload_range

    # Filter by site and payload range
    if site_dropdown == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= min_payload_range) & 
                                (spacex_df['Payload Mass (kg)'] <= max_payload_range)]
        title_site = "All Sites"
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == site_dropdown) & 
                                (spacex_df['Payload Mass (kg)'] >= min_payload_range) & 
                                (spacex_df['Payload Mass (kg)'] <= max_payload_range)]
        title_site = site_dropdown

    # Handle empty data
    if filtered_df.empty:
        fig = px.scatter(title='No data available for the selected filters')
        fig.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            annotations=[dict(
                text="No data available for the selected filters",
                xref="paper", yref="paper",
                showarrow=False,
                font=dict(size=16)
            )]
        )
        return fig

    # Add jitter to y-axis to prevent point overlap
    plot_df = filtered_df.copy()
    plot_df['jitter'] = plot_df['class'].apply(lambda x: x + np.random.normal(0, 0.05))

    fig = px.scatter(
        plot_df,
        x='Payload Mass (kg)',
        y='jitter',
        color='Booster Version Category',
        title=f'Payload Success Rate for {title_site}',
        labels={'Payload Mass (kg)': 'Payload Mass (kg)'}
    )

    # Set y-axis to show success/failure clearly
    fig.update_yaxes(
        tickvals=[0, 1],
        ticktext=['Failure (0)', 'Success (1)']
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run()
