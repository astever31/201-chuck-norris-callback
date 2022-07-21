######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['angry', 'happy', 'sad']
githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
#image1='mad-pika.jpg'
list_of_images=['mad-pika.jpg', 'happy-pika.jpg', 'sad-pika.jpg']
heading1='Chuck Norris execution method'
mydict={list_of_choices[i]:list_of_images[i] for i in range(len(list_of_choices))}

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Chuck'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': n} for i, n in mydict.items()],
                value=list_of_images[0],
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return html.Img(src=app.get_asset_url(whatever_you_chose), style={'width': 'auto', 'height': '10%'}) #f'Chuck Norris will now execute you with a {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)