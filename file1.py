# In the "Customer" class =>  The following subtasks must be implemented:
# 1.1: [2] add a class variable "customer_count" to the class "Customer" initiated with 0 that represents
#      the number of instances, and increment it each time, when a new instance is generated
# 1.2: [2] add a method "__del__" to the class "Customer" that decrements
#      "customer_count" when called

from datetime import datetime as dtime
from typing import List
from random import sample, choice, seed

class Customer:
    _monthly_rate = 50

    def __init__(self, id):
        self.cust_id = id
        self.date_time_of_creation: dtime = dtime.now()

    def __str__(self):
        return (f"StreamCust ID: {self.cust_id}, "
                f"date_time_of_creation: {self.date_time_of_creation}")

    # Use this method as a 'Hint' for one of the later tasks
    def __repr__(self):
        return (f"StreamCust ID: {self.cust_id}, "
                f"date_time_of_creation: {self.date_time_of_creation}")


#######################################################################
#                                                                     #
#                                 TASK 2   (22 Points)                #
#                                                                     #
#######################################################################

# In the "StreamCust" class =>  The following subtasks must be implemented:
# 2.1: [2] let the class "StreamCust" inherit from "Customer" all attributes.
# 2.2: [6] implement a getter/setter method for _stream_volume_record[]
# 2.3: [7] implement a getter/setter property "stream_volume" for _stream_volume_sum that:
#     a. [2] returns the _stream_volume_sum in a getter property
#     b. [5] raises in a setter property "ValueError" exception with the message
#            "ERROR: irregular stream value." if the value is less than zero (<0)


class StreamCust():
    _stream_rate = 0.2

    def __init__(self, id):
        # Hint: something to do here ...?
        self._stream_volume_record = [0]
        self._stream_volume_sum = 0

    def __str__(self):
        return (f"StreamCust ID: {self.cust_id}, "
                f"date_time_of_creation: {self.date_time_of_creation}, "
                f"_stream_volume_record: {self._stream_volume_record}, "
                f"_stream_volume_sum: {self._stream_volume_sum}")

    def anonymous01(self):
        self._stream_volume_record = [9999, 8888, 7777, 6666, 5555, 4444, 3333]



#######################################################################
#                                                                     #
#                                 TASK 3   (30 Points)                #
#                                                                     #
#######################################################################

# In the function "main_program()"  =>  The following subtasks must be implemented:
# 3.1 to 3.8 => follow the commands in the function "main_program()" code below!!

def main_program():
    seed(1)

    c1 = Customer(1010)  # self-selected 'cust_id': 1010
    c2 = Customer(2020)  # self-selected 'cust_id': 1010

# Task 3.1: [4]
    # Implement a (free) function 'random_cust_id_number(number)', which returns 'number' (e.g. 12)  elements
    # of int-values as a list between 5000 and 9999.
    # Replace the "fixed" list below (i.e. to the right side of the '=') with a correct
    # function call 'random_cust_id_number(12)'.
    # Hint: use the sample(...) function in the module 'random'.

    # If you cannot solve task 3.1 then use the list below (=generated_random_cust_id_numbers)
    # for the next tasks.

    ##########################
    # your work (program the free function 'random_cust_id_number(number)'.
    # Choose the correct place for your free function ... (not here!!!)
    # Replace the right part (right side of the '=') of the next line with your code.
    ##########################

    generated_random_cust_id_numbers = [6100, 9662, 5516, 7089, 5965, 9058, 8682, 8868, 8109, 6719, 5768, 8996]

    print("3.1: generated_random_numbers: ", generated_random_cust_id_numbers)

# Task 3.2: [3]
    print("3.2: Program a List comprehension")
    # Goal: We want create a 'number' of objects from the StreamCust class.
    # Replace the "fixed" list of StreamCust object below (i.e. to the right side of the '=') with
    # a 'list comprehension'!
    # Hint: Use 'generated_random_cust_id_numbers' from Task 3.1 in the 'list comprehension'.

    ##########################
    # your work: program the 'list comprehension'.
    # Replace the list below with your 'list comprehension'.
    ##########################

    sc_list = [StreamCust(6100), StreamCust(9662), StreamCust(5516), StreamCust(7089), StreamCust(5965), \
               StreamCust(9058), StreamCust(8682), StreamCust(8868), StreamCust(8109), StreamCust(6719), \
               StreamCust(5768), StreamCust(8996), ]

    # If you can't program the 'list comprehension', use the 'sc_list' above for all next tasks!

# Task 3.3: [2]
    print("3.3 Print Customer objects: ")
    # Print the objekct c1 and c2

    # Hint: The output results will be something like:
    # StreamCust ID: 1010, date_time_of_creation: 2023-12-19 07:12:53.941328
    # StreamCust ID: 2020, date_time_of_creation: 2023-12-19 07:12:53.941338

    ##########################
    # your work: Output c1 and c2
    ##########################


# Task 3.4: [2]
    print("3.4 Output the attributs of the twelve StreamCust objects:")
    # Output the  of the twelve "StreamCust" objects in 'sc_list'.

    # Hint: You can do it
    #       a) with a list comprehension
    #       b) with a "__repr__()" method in the class "StreamCust"
    # You decide for yourself which of the two variants you implement.

    # The output of Task 3.4 has to be in following form (on ONE line only!):
    # [StreamCust ID: 6100, date_time_of_creation: 2024-01-10 10:45:59.136638, _stream_volume_record: [0], _stream_volume_sum: 0, StreamCust ID: 9662, .... and so on!!   ]
    # or
    # ['StreamCust ID: 6100, date_time_of_creation: 2023-12-19 10:49:36.722166, _stream_volume_record: [0], _stream_volume_sum: 0', 'StreamCust ID: 9662, ... and os on!!   ']

    ##########################
    # your work!
    ##########################

    print("3.4 Attributs of the objects of 'sc_list': ")
    print(sc_list)

# Task 3.5: [5]
    print("3.5 Generate 'generate_stream_volume_record_list()' ")
    # Generate a (free) function 'generate_stream_volume_record_list()' which returns
    # a random list of size 5 to 20 elements.
    # The elements of the list should be 'int' values in the range of 500 to 10000.

    # Hint 1: Use 'sample()' and 'choice()' from the 'random' module.

    # Hint 2: Examples of possible returns of the (free) function 'generate_stream_volume_record_list()':
    # stream_volume_record_list_sample = [9999, 8888, 7777, 6666, 5555, 4444, 3333]
    # or (second example):
    # stream_volume_record_list_sample = [6719, 3939, 2037, 8493, 964, 6886, 7590, 534, 7797, 4863, 4248, 865]
    # ... and so on!

    # Attention:
    # If you can't implement the 'generate_stream_volume_record_list()' function,
    # use always the 'fixed' list [9999, 8888, 7777, 6666, 5555, 4444, 3333] for
    # the variable 'stream_volume_record_list_sample' in the following tasks for all StreamCust objects.

    if "generate_stream_volume_record_list" in globals():
        stream_volume_record_list_sample = generate_stream_volume_record_list()
    else:
        stream_volume_record_list_sample = [9999, 8888, 7777, 6666, 5555, 4444, 3333]

    print("3.5 Return of 'generate_stream_volume_record_list()': ", stream_volume_record_list_sample)

# Task 3.6:  [3]
    print("3.6 Fill the 'stream_volume_record[]' attribute with a randomly generated list.")
    # Fill the '_stream_volume_record[]' attribute of every StreamCust object in 'sc_list' \
    # with a randomly generated list from the (free) function 'generate_stream_volume_record_list()'

    # Hint:
    # If you couldn't program the (free) function 'generate_stream_volume_record_list()' in Task 3.5
    # use the given list from variable 'stream_volume_record_list_sample' (= [9999, 8888, … , 4444, 3333])
    # AND
    # use the following two lines as a starting point for Task 3.6:
    for sc in sc_list:
        sc.anonymous01()
        # Your 'remaining work' for Task 3.6: fill in the 'stream_volume_record[]' attribute with
        # a randomly generated list

    # If you solved Task 3.5:  Comment out the code above and use following uncommented code:
    # for sc in sc_list:
    #     stream_volume_record_list_sample = generate_stream_volume_record_list()
    #      # Your 'remaining work' for Task 3.6: fill in the 'stream_volume_record[]' attribute with
    #      # a randomly generated list

    ##########################
    # your work!    correct/replace the code above!
    ##########################

# Task 3.7:  [5]
    print("\n3.7 Output of 'static' method 'list_output()': ")
    # Generate a 'static' method 'list_output()' in the class StreamCust.
    # The method 'list_output()' must output the actual values of all attributes
    # of all StreamCust objects in the 'sc_list'.
    # Each object in 'sc_list' must be printed on ONE line!!


    # Hint: The correct output should be like:   (every object in 'sc_list' on ONE line)
    # sc 1:  StreamCust ID: 6100, date_time_of_creation: 2023-12-17 22:32:13.058263, _stream_volume_record: [9999, 8888, 7777, 6666, 5555, 4444, 3333], _stream_volume_sum: 0
    # sc 2:  StreamCust ID: 9662, date_time_of_creation: 2023-12-17 22:32:13.058265, _stream_volume_record: [6719, 3939, 2037, 8493, 964, 6886, 7590, 534, 7797, 4863], _stream_volume_sum: 0
    # sc 3:  StreamCust ID: 5516, date_time_of_creation: 2023-12-17 22:32:13.058266, _stream_volume_record: [9370, 650, 6745, 4048, 7415], _stream_volume_sum: 0
    # ... and so on!

    print("     wrong output: ", sc_list)  # this code is wrong here! replace!
    ##########################
    # your work!      correct/replace the of code above. Use your list_output(...) function.
    ##########################


# Task 3.8  [6]
    print("\n3.8 Complete all methods and variables with meaningful Python annotations!")
    # Complete all methods and variables with meaningful Python annotations (Type Hints)
    # (like the PEP 484-Standards).
    ##########################
    # your work!      (in the complete code of this exam!)
    ##########################




if __name__ == "__main__":
    main_program()
