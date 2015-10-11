import rauth
import time

def main():
	# user preferences
	total_cost = 0
	number_of_rides = 0
def attractionSearch(locations=[(39.98,-82.98)],type='attractions'): #locations in the form   [(39.98,-82.98)] type = "attractions"
	# location will be taken in from somewhere ####################################################FIX

	api_calls = []

	for lat, long in locations:
		# call a search for attractions
		params = get_search_parameters(lat,long,type)
		api_calls.append(get_results(params))

		# Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)

	place=[]
	if (type == 'attractions'):
		x = 0
	else:
		x = 1
	for api in api_calls[x]['businesses']:
		place += [{'type':type,'name':api['name'],'rating':api['rating'],'location':api['location'],'rating_img_url':api['rating_img_url'],'image_url':api['image_url'],'mobile_url':api['mobile_url'],'display_phone':api['display_phone'],'categories':api['categories']}]
	#
	# for api in api_calls[1]['businesses']:
	# 	place += [{'type':'restaurants','name':api['name'],'rating':api['rating'],'location':api['location'],'rating_img_url':api['rating_img_url'],'image_url':api['image_url'],'mobile_url':api['mobile_url'],'display_phone':api['display_phone'],'categories':api['categories']}]
	#
	return place
	#restaurant

def sendToUber(*args): # does stuff Wait TILL WE GEt uber and shit done
	print "hi"

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
	params["limit"] = "20"

	return params

if __name__=="__main__":
	main()
