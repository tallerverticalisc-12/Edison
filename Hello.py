from flask import Flask
import json
import requests

@app.route('/sensor')

def hello():
    return "Hello World"

if __name__ == '__main__':
	app.run( 
		host="http://45.40.137.37",
		port=int("88")
	)