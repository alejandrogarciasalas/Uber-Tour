import rauth
import time

def main():
#	# user preferences
#	total_cost = 0
#	number_of rides = 0

	# location will be taken in from somewhere
	locations = [(39.98,-82.98)]
	api_calls = []

	for lat, long in locations:
		# call a search for attractions
		params = get_search_parameters(lat,long,"attractions")
		api_calls.append(get_results(params))

		# call another search for restaurants
		params = get_search_parameters(lat,long,"restaurants")
		api_calls.append(get_results(params))

	# Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)

	## Do other processing

def get_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = "PeVRBJoCVCl6bkuE_4mXtA"
	consumer_secret = "v_K-1tGeQgoT-iwAXFr1AnkVCuw"
	token = "7O0C7eX76WlTD-AiWtP62Vgoj4q4ErdI"
	token_secret = "qUrbQv3860LOlYS_Mzz6sFFX_vw"

	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)

	request = session.get("http://api.yelp.com/v2/search",params=params)

	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()

	return data

def get_search_parameters(lat,long,term):
	#See the Yelp API for more details
	params = {}
	params["term"] = term
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "3"

	return params

if __name__=="__main__":
	main()
