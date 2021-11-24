# Planck-s-Tech-Assignment




#    description

The main file is app.py all the routes located their. 
with help of thread every 24 hours the server updates the json file.

The conrollers.py file purpose is to do the logical things of searching for the appropriate data. it do it, with the help of GetDb.py to read json file from their.

The GetDb.py his goal to update data from the end-point and to read the data from the file

The example_order.json is example for post order. (delete before the calculate from their)



# How does it work?

downlowd all the file. ( git clone https://github.com/meirfuces/Planck-s-Tech-Assignment.git) 

run app.py

check the route

Get:
http://127.0.0.1:5000/drinks

http://127.0.0.1:5000/drink/2055843

http://127.0.0.1:5000/pizzas

http://127.0.0.1:5000/pizza/2055830

http://127.0.0.1:5000/desserts

http://127.0.0.1:5000/dessert/2055835

Post:

http://127.0.0.1:5000/order   (send a json file)




