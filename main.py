import json
import scraper
import sys

from flask import Flask, render_template, request
import pandas as pd

import requests

app = Flask(__name__)

#browser will not cache static assets that are served by Flask
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/hello')
def hello():
    return 'Hello, another World'


@app.route('/',methods = ['POST', 'GET'])
def userInput():
	query = "mord"
	if request.method == 'POST':
		query = request.form.to_dict() 
		query = query.get('Name') #get keyword user entered
		print(query)

	with open('./static/nodes.json') as json_data:
		nodes = json.load(json_data)
		nodes2 = []
		#print(nodes)
		for item in nodes:
			#print(item.get("keyword"))
			if item.get("keyword") == query:
				#print('item contains query')
				nodes2.append(item)
	print('nodes2', nodes2)
	with open('./static/edges.json') as json_data:
		edges = json.load(json_data)
		#print(d)
	#d = {"testdata":2}
	return render_template("index.html", d=[nodes, edges, query])
		
#return render_template("result.html",result = result)

if __name__ == "__main__":
	app.run(debug=True)

#sources:
#https://medium.com/@wahyudihandry/how-to-build-web-scraping-using-beautifulsoup-and-flask-part-i-ca38a167c236
#https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
#https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env