from flask import Flask, render_template, request
app = Flask(__name__)
import os
import yelp_api

@app.route("/")
def index():
	address = request.values.get('address')
	resturants = None
	if address:
		resturants = yelp_api.get_businesses(address)
	return render_template('index.html', resturants=resturants)

@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)