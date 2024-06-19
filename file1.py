hellooo


# < solution for Task 1a >

car_trips = [500.455, 23.45, 986.4567, 12.55, 234.8675, 0.621331, 32.6794]

car_trips_new = [trip / 0.621371 for trip in car_trips]

print(1, car_trips_new)


# < solution for Task 1b >

formated_car_trips_new = [round(trip, 1) for trip in car_trips_new]

print(2, formated_car_trips_new)
