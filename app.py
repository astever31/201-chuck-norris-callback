######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['angry', 'happy', 'sad']
githublink = 'https://github.com/astever31/201-chuck-norris-callback'
#image1='mad-pika.jpg'
list_of_images=['mad-pika.jpg', 'happy-pika.jpg', 'sad-pika.jpg']
heading1='The various emotions of Pikachu'
mydict={list_of_choices[i]:list_of_images[i] for i in range(len(list_of_choices))}
tabtitle='Pikachu'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': list_of_choices[i], 'value': i} for i in list_of_choices],
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
    return html.Img(src=app.get_asset_url(mydict.get(whatever_you_chose)), style={'width': 'auto', 'height': '10%'}) 

@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'You made Pikachu {list_of_choices[whatever_you_chose]}!'

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)