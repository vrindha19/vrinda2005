# create threading

# import threading

# def print_cube(num):
#     print("clube:{}".format(num*num*num))
    
# def print_square(num):
#     print("square:{}". format(num*num))

# if __name__ =="__main__":
#     t1= threading.Thread(target=print_square,args=(10,))
#     t2= threading.Thread(target=print_cube,args=(10,))

#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Done!")


#  thread using decorators 


# import threading

# # Decorator function for threading
# def run_in_thread(fn):
#     def run(*args, **kwargs):
#         thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
#         thread.start()
#         return thread
#     return run


# # Example of a function that will be executed in a separate thread using the decorator
# @run_in_thread
# def example_function(name, times):
#     for i in range(times):
#         print(f"Hello, {name} - {i}")

# Usage of the decorated function
# example_function("Alice", 5)
# example_function("Bob", 3)


# timer objects in python 
  
# import threading 
# def gfg(): 
#     print("GeeksforGeeks\n") 
  
# timer = threading.Timer(2.0, gfg) 
# timer.start() 
# print("Exit\n") 

# timer cancel


# import threading 
  
# def gfg(): 
#     print("GeeksforGeeks\n") 
  
# timer = threading.Timer(5.0, gfg) 
# timer.start() 
# print("Cancelling timer\n") 
# timer.cancel() 
# print("Exit\n") 









