import time

my_list = ["cat", "dog", "bird", "aligator"]

def my_decorator(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        print("Started: ",time1)
        func(*args, **kwargs)
        time2 = time.time()
        print("Ended: ", time2)
        print('{:s} took {:.3f} ms'.format(func.__name__, (time2 - time1) * 1000.0))
    return wrapper

@my_decorator
def other_function(my_list):
    my_ordered_list = sorted(my_list, key=lambda x: x[-1])
    print(my_ordered_list)

other_function(my_list)