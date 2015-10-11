def main():
    attraction_list = # get 20 locations from yelp-process file
    schedule_list = []
current_location = start_location (get from somewhere)
end_location = (get from somewhere)

FunctionSort - sorts by our criteria
    remove the first element
    sort by (popularity) / (distance from current location)
    return the new list

(while loop - len(attraction_list) > 0) calculate if condition
    # if true, it analyzes the first element (e.g. the optimal destination)
    if(time spent + time to destination + time at the destination + time to the end < max_time)
        add destination to schedule_list
        set current to destination
        decrement time (time to destination + time at destination)
        decrement cost (cost of Uber to destination)
    attraction_list = attraction_list.functionSort()

add the end to the schedule_list
