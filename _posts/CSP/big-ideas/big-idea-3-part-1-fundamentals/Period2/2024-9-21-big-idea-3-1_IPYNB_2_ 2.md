---
layout: post
title: 3.1-P2 Variables and Assignments
description: This lesson explains how variables are abstractions used to represent and store data.
categories: ['Python', 'Javascript']
permalink: /csp/big-idea/p2/3-1
menu: nav/csp_units/csp_unit3_p2_fundamentals.html
author: Arhaan, Mihir, Akshaj, Keerthan
toc: True
comments: True
---

# **Introduction to Variables**

---

## What is a Variable?

A **variable** is like a container that holds information. You can store data in a variable and use it later in your program.

For example, if you want to store a person's name or age, you can use variables to do that.

---

## Video Help 

<div>
    <p> Click the following button to get extra help on loops in coding </p>
</div>
<a href="https://www.youtube.com/watch?v=KpJ385shzgM">
<button class="button button1">Variables Video</button>
</a>


## Creating Variables

You can create a variable and assign a value to it using the assignment operator `=`.

### Example:
```python
# Python Example
name = "Alice"  # This is a string variable
age = 15        # This is an integer variable

// JavaScript Example
let name = "Alice";  // This is a string variable
let age = 15;        // This is an integer variable


## Using Variables in Programs

Once you have created a variable, you can use it throughout your program.





```python
# Define variables
name = "John"  # Replace with the desired name
age = 25       # Replace with the desired age

# Print statements
print("My name is", name)
print("I am", age, "years old.")


```

    My name is John
    I am 25 years old.



```python
%%js
// JavaScript Example
console.log("My name is " + name);
console.log("I am " + age + " years old.");

```


    <IPython.core.display.Javascript object>


## Naming Variables
When you create variables, it's important to choose good names. Here are some tips:

Be Descriptive: Choose names that describe the data they hold, like age or favorite_color.

Use Camel Case: For multi-word names, use camel case (e.g., favoriteColor).

Avoid Spaces and Special Characters: Stick to letters, numbers, and underscores.



```python
# Creating and using variables
city = "New York"
population = 8419600

print("The city is", city)
print("The population is", population)

```

    The city is New York
    The population is 8419600



```python
%%js
// Creating and using variables
let city = "New York";
let population = 8419600;

console.log("The city is " + city);
console.log("The population is " + population);

```


    <IPython.core.display.Javascript object>

