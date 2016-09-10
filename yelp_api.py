from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_businesses(address):

	auth = Oauth1Authenticator(
		consumer_key=os.environ['YELP_CONSUMER_KEY'],
		consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
		token=os.environ['YELP_TOKEN'],
		token_secret=os.environ['YELP_TOKEN_SECRET']
		)

	client = Client(auth)

	params = {
    	'term': "food",
    	'lang': 'en',
    	'limit': '3'
    	}

	response = client.search(address, **params)

	businesses = []

	for business in response.businesses:
		# print(business.name, business.rating, business.phone)
		businesses.append({"name": business.name, 
			"rating": business.rating, 
			"phone": business.phone,
			"image": business.image_url
		})
	
	#return("The top 3 recommended resturants for {}, are: {}, {}, and {}".format(address, businesses[0]['name'], 
		#businesses[1]['name'], businesses[2]['name']))

	return businesses

# businesses = get_businesses('Arlington, Virginia', 'food')

