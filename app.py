######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['happy', 'angry', 'sad']
githublink = 'https://github.com/astever31/201-chuck-norris-callback'
#image1='happy-pika.jpg'
list_of_images=['happy-pika.jpg', 'angry-pika.jpg', 'sad-pika.jpg']
heading1='The various emotions of Pikachu'
tabtitle='Pikachu'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div(children=[
    html.H2(heading1),
    dcc.Dropdown(id='your-input-here',
                #options=[{'label': i, 'value': n} for i in list_of_choices for n in list_of_images],
                options=[
                {'label':list_of_options[0], 'value':list_of_images[0]},
                {'label':list_of_options[1], 'value':list_of_images[1]},
                {'label':list_of_options[2], 'value':list_of_images[2]},
                {'label':list_of_options[3], 'value':list_of_images[3]},
                ],
                value=list_of_choices[4]
                ),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return html.Img(src=app.get_asset_url(whatever_you_chose), style={'width': 'auto', 'height': '10%'}),
f'You made Pikachu {whatever_you_chose}!'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
