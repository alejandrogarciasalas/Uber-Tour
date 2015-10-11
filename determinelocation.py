from app import *

def get_schedule(data):
    """ Returns the sorted list of attractions. """
    user_preferences = data['user_preferences']
    attraction_list = data['attractions']
    current_location = user_preferences['initial_location']
    end_location = user_preferences['final_location']
    MAX_TIME = user_preferences['max_time']
    time_left = MAX_TIME
    total_cost = 0
    schedule_list = []

    while len(attraction_list) > 0: # calculate if condition
        # if true, it analyzes the first element (e.g. the optimal destination)
        attraction = attraction_list[0]
        time_and_price_to_attraction = time_and_price_estimate(
            current_location['latitude'],
            current_location['longitude'],
            attraction['location']['coordinate']['latitude'],
            attraction['location']['coordinate']['longitude'])
        time_to_attraction = time_and_price_to_attraction['time']
        price_to_attraction = time_and_price_to_attraction['price']

        time_and_price_to_end_location = time_and_price_estimate(
            attraction['location']['coordinate']['latitude'],
            attraction['location']['coordinate']['longitude'],
            end_location['latitude'],
            end_location['longitude']
        )
        time_to_end_location = time_and_price_to_end_location['time']
        price_to_end_location = time_and_price_to_end_location['price']

        total_attraction_time = time_to_attraction + TIME_AT_DESTINATION
        if(time_left - total_attraction_time - time_to_end_location >= 0):

            schedule_list.append(attraction)
            current = attraction
            max_time -= total_attraction_time
            total_cost += price_to_attraction

        attraction_list = sort_attractions(attraction_list)

    schedule_list.append(end_location)
    total_cost += price_to_end_location
    total_time = MAX_TIME - time_left
    return {'schedule' : schedule_list, 'time' : total_time, 'cost' : total_cost}

def sort_attractions(attraction_list):
    attraction_list.pop(0) # remove the first element
    attraction_list.sort(key=attraction_score) # sort by (popularity) / (distance from current location)

def attraction_score(attraction):
    return attraction['rating'] / attraction['distance']
