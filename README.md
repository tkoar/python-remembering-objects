
# Python Remembering Objects Lab

## Introduction
Okay, we have done a good amount of work with classes and instances. At this point we are able to successfully define all kinds of classes and instance methods. We can initialize instance objects and operate on them until the cows come home. However, we haven't totally been designing our classes to keep track of all these instance objects. That seems like an important piece of the puzzle on our road to Object Oriented Python mastery, right? That's right! We will explore using Python's class methods and class variables in order to **remember** *all* of the instance objects a class instantiates.

## Objectives
* Understanding why we need to Persist all of our class's instance objects 
* Learn to use class methods and class variables to persist and access instance objects produced by a class
* Operate on each isntance object created by a class

## Why Persist *All* Instance Objects 

Let's take for example a car manufacturer. Cars are created with a `make`, `model`, and `color`. We could think of all types of questions we might want to ask about the collection of cars we manufacture. What model car did we produce the most? What color car is currently trending? Or even more straight forward, how many of a certain model car have we produced? How would our classes know how to answer these very difficult questions without being able to recall each car instance object it has created? 

To start, we will define a Car class that can instantiate car instances with the instance variables `_make`, `_model`, and `_color`. We won't need to change the make or model of a car after its created because we can't do that in the real world, but we might want to alter the color, which is possible. So, let's define instance methods to read (get) all three attributes and an instance method to write (set) the color of a car.


```python
class Car:
    
    def __init__(self, make, model, color):
        self._make = make
        self._model = model        
        self._color = color
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color
        return self._color
    
```


```python
# Here we are creating some jeeps -- 13 to be exact.
# We are using some lists with data describing different jeeps
# to create a new list of car instance objects.
# Run this cell to see a list of all the car instance objects we are creating below

def make_cars():
    manufacturer = "Jeep"
    models = ["Wrangler", "Grand Cherokee", "Cherokee", "Compass"]
    colors = ['green', 'red', 'blue', 'grey']
    num_each_model_to_make = [1, 4, 5, 3]
    index = 0

    for num in num_each_model_to_make:
        for i in list(range(num)):
            car = Car(manufacturer, models[index], colors[index])
            print(vars(car))
        index += 1
        
make_cars()
```

## How to Persist Each New Car Instance Object

Okay, we have all of our shiny new jeeps displayed in some beautiful dictionary notation above. How can we, **without looking at the code above**, know how many blue cars have been made? Maybe a bit more interesting of an insight, how can we know what the distribution of models manufactured is? Well, put simply, we can't. These cars are being created and promptly pushed into a black hole, never to be seen or heard from again. :( 

So, how do we fix this? Well, using our knowledge of class variables, we can create a class variable called **`_all`**  for our classes that points to a list, which is where we will append each of our new instance objects. That way, we will have a way to always access each instance object we've ever made in a particular class.

Let's try it out with our car class.


```python
class Car:
    
    _all = []
    
    def __init__(self, make, model, color):
        self._make = make
        self._model = model        
        self._color = color
        self.save()
        
    @classmethod
    def all(cls):
        return cls._all
        
    def save(self):
        Car.all().append(self)
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color
        return self._color
```


```python
print(len(Car.all()))
make_cars()
print(len(Car.all()))
```

Awesome! Now our class is using a class variable to keep track of all these new car instance objects. 

Let's unpack what is happening above. We have basically our same class as we had when we started, but we've added three (3) things. The first thing we added was our class variable `_all`. This is our list that we use to hold all of our car instance objects. Second we have our class method `all` that returns the class variable, `_all`. Alright, those both seem very straightforward. We are using our class method to return the class variable, just as we do with our instance variables and instance methods. 

Now, the third thing we've changed about our class is we have added an instance method called `save` which we call on our instance object in our `__init__` method. The `save` method simply calls the class method `all()` to return the class variable `_all`, and it appends the instance object, `self`, to our class variable `_all`. 

As always, we try to name our instance and class variables and methods so that they describe what they are or what they do. The naming convention for a class variable that keeps track of all instance objects of that class is `_all`, and the convention for accessing that variable is by defining a class method that returns that class variable. The naming convention for an instance method that *persists* or adds an instance to our program's memory, is `save`. 

To sum up, now when we initialize a new isntance object, we are saving it by calling the instance method `save` and then adding it to our class variable, `_all`.

## Operating on `_all` Instance Objects

Now that we know how to save and access each of our instance objects, let's see how we can really use this information. We mentioned wanting to know the most popular color for a Jeep or what the distribution is like for each model that is manufactured by Jeep. Well, let's check it out!

We are going to follow best practices and create a method *inside* our class to answer these questions. Since this is a question about the class as a whole, we will be making class methods to answer these questions.


```python
class Car:
    
    _all = []
    
    def __init__(self, make, model, color):
        self._make = make
        self._model = model        
        self._color = color
        self.save()
        
    @classmethod
    def all(cls):
        return cls._all
        
    def save(self):
        Car.all().append(self)
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color
        return self._color
    
    @classmethod
    def most_popular_color(cls):
        color_histogram = {}
        most_popular_color = ""
        num_cars = 0
        for car in cls.all():
            if not car.color in color_histogram:
                color_histogram[car.color] = 1
            else:
                color_histogram[car.color] += 1
        for key, value in color_histogram.items():
            if num_cars < value:
                most_popular_color = key
                num_cars = value
        return most_popular_color
    
    @classmethod
    def make_histogram_of_models(cls):
        model_histogram = {}
        for car in cls.all():
            if not car.model in model_histogram:
                model_histogram[car.model] = 1
            else:
                model_histogram[car.model] += 1
        return model_histogram

make_cars()
```


```python
Car.most_popular_color()
```


```python
import plotly as py
import plotly.graph_objs as go

car_histogram = Car.make_histogram_of_models()
py.offline.init_notebook_mode(connected=True)

trace = {
    'type': "bar", 
    'x': list(car_histogram.keys()), 
    'y': list(car_histogram.values())
}

py.offline.iplot({'data': [trace]})
```

## Summary


In this lab, we introduced using the class variable `_all` to create a single reference to all intance objects of a class. We then introduced the Python conventions for accessing this list of instance objects by using a class method, `all`, and using an instance method, `save` to append instance objects to the `_all` list. These conventions ensure a clear and concise understanding of common operations that are performed in Object Oriented Python Programs. Once we have our classes set up in this fashion, we can then focus on doing some more interesting things like creating class methods to return the most popular attribute value like **color** for all cars, or even plot the distribution of instance objects based on those values. 
