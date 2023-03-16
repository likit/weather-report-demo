from flask import Flask, render_template, request, jsonify, redirect
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    city = request.form.get('city')
    print(city)
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    api_key = 'da7d62b71556b75f60a2d770210dc664'
    params = {'q': city, 'appid': api_key}
    r = requests.get(url, params=params)  # api call
    data = r.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    return redirect(f'/report?lat={lat}&lon={lon}')
  else:
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
  lat = request.args.get('lat')
  lon = request.args.get('lon')
  return render_template('weather.html', lat=lat, lon=lon)


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
