
# Python Remembering Objects Lab

## Introduction
Okay, we have done a good amount of work with classes and instances. At this point we are able to successfully define all kinds of classes and instance methods. We can initialize instance objects and operate on them until the cows come home. However, we haven't really thought about we keep track of all these instance objects yet. Seems like an important piece of the puzzle on our road to Object Oriented Python mastery, right? That's right! The next time we create a Person class and want to keep track of all these people, or as we like to call them person instance objects, we will be able to! We will explore using Python's class methods and class variables in order to **remember** the instance objects a class instantiates.

## Objectives
* Understand how classes remember, or store, the instance objects they instantiate
* Practice using class methods and class variables to persist instance objects produced by a class

## Instructions

Let's take for example a car manufacturer. Cars are created with a `make`, `model`, and `color`. We could think of all types of questions we might want to ask about the collection of cars we manufacture. What model car did we produce the most? What color car is currently trending? Or even more straight forward, how many of a certain model car have we produced? How would our classes know how to answer these very difficult questions without being able to recall all car instance objects it has ever created? 

To start, we will define a Car class that can instantiate cars instances with the instance variables `_make`, `_model`, and a `_color`. We won't need to change the make or model of a car after its created because we can't do that in the real world, but we might want to alter the color, which is possible. So, let's define instance methods to read (get) all three attributes and an instance method to write (set) the color of a car.

> **note:** remember to load the autoreload extension from IPython
```python
%load_ext autoreload
%autoreload 2
```


```python
from car import Car
```


```python
new_car = Car("Jeep", "Grand Cherokee", "Green")
new_car
```


```python
# oh no! we wanted a blue car. let's change the color:
new_car.color = "Blue"
new_car.color # Blue
```

Great! Now, to remember the instances of a class and keep them in one place, we will use a list. Let's define a class variable called `_all` and assign it to an empty list.


```python
Car._all # []
```

Then, let's write a class method with the `@classmethod` decorator and name it `save`. Remember, in order to reference the class, we use the parametere `cls` in our method definition in place of `self`. The `save` class method will also need to know what it is saving, so, the second argument will be the instance object we are appending to our `_all` list. Once the instance object is added to our list, it should return the newly updated `_all` list.


```python
Car.save(new_car) # [<__main__.Car object at 0x1068dd7f0>]
```

## Summary

