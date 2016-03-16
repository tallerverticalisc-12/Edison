from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/sensor')

def hello():
    return "Hello World"

if __name__ == '__main__':
	app.run( 
		host="http://45.40.137.37",
		port=88
	)