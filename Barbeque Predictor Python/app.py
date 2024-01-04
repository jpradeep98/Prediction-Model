import requests
from flask import Flask, render_template, request

app = Flask(__name__)
api_key = '7ed40c4c3b025592d22300be33c1ca6f'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_time', methods=['POST'])
def suggest_time():
    city = request.form['city']
    # temperature = float(request.form['temperature'])
    # weather = request.form['weather'].lower()
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        tempCelcius = round(- 273.15 + temp, 1)
        citytemperature = f"{tempCelcius} Celsius"
        cityweather = desc
        
    else:
        citytemperature = 'Error Retrieving Data. Try Again'

    if tempCelcius > 20:
        suggestion = 'Good time for a Barbeque'
    elif cityweather == 'rain' and tempCelcius > 18:
        suggestion = 'You can still take a chance and start Barbeque. Keep an umberalla handy if it rains'
    else:
        suggestion = 'Not a good time for a Barbeque! Better luck next time!!!!'

    return render_template('index.html', suggestion=suggestion, city = city, citytemperature = citytemperature, cityweather = cityweather )

if __name__ == '__main__':
    app.run(debug=True)