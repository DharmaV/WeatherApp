from flask import Flask, request
from flask import render_template
from datetime import datetime
import urllib.request
import json
import os
import urllib.parse as urlparse

app = Flask(__name__)
apiKey='d1olagX1xAYHxFi6TqEKbpuAD1gukAuO'
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Sairam sai baba',
        year=datetime.now().year,
    )

@app.route('/location',methods=['GET','post'])
def getLocations():
    parsed = urlparse.urlparse(request.url)
    searchTxt=urlparse.parse_qs(parsed.query)['searchtext'][0]
    locationApiUrl='http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey='+apiKey+'&q='+searchTxt+'&language=en-us'
    imageApi='http://dataservice.accuweather.com//imagery/v1/maps/radsat/1024x1024/125887?apikey=d1olagX1xAYHxFi6TqEKbpuAD1gukAuO'
        #searchtext=request.json['searchtxt']
   # with urllib.request.urlopen(imageApi) as imageApiresult:
    #    data = json.loads(imageApiresult.read().decode())
     #   print(data)

    with urllib.request.urlopen(locationApiUrl) as locationsSearch:
        data=json.loads(locationsSearch.read().decode())
        options = []
        for city in data:
            lblText=city['Type']+':'+city['LocalizedName'] + ' -  Country:'+city['Country']['LocalizedName']
            options.append('{ "label":"'+ lblText+'","value":"'+city['Key']+'"}')
            print('{ "label":"' +city['Type']+':'+city['LocalizedName']+'","value":"'+city['Key']+'"}')

        print(data)
        s = ','
        return '['+s.join(options)+']'
# return  '[{ "value": "sairam","label": 6}]'

#def display():
 #   return "sairam"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
