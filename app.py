######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['happy', 'angry', 'sad']
githublink = 'https://github.com/astever31/201-chuck-norris-callback'
#image1='happy-pika.jpg'
list_of_images=['happy-pika.jpg', 'mad-pika.jpg', 'sad-pika.jpg']
heading1='The various emotions of Pikachu'
#mydict={list_of_choices[i]:list_of_images[i] for i in range(len(list_of_choices))}
tabtitle='Pikachu'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='image-output', src=app.get_asset_url(list_of_images[0])),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': list_of_choices[i], 'value': i} for i in range(len(list_of_choices))],
                value=list_of_choices[0],
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
    return f'You made Pikachu {list_of_choices[whatever_you_chose]}!'

@app.callback(dash.dependencies.Output('image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])#, style={'width': 'auto', 'height': '10%'}

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)