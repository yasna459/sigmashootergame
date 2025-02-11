---
toc: False
comments: True
layout: post
title: 3.2-P2  Data Abstraction
description: Student led teaching on Abstraction. Teaching how various data types can use abstraction for computational efficiency.
permalink: /csp/big-idea/p2/3-2/
categories: ['CSP Big Ideas']
author: Nikhil Maturi, Yash Parikh, Neil Chandra, Rohan Bojja (P.2)
menu: nav/csp_units/csp_unit3_p2_fundamentals.html
---

## Practice Quiz (CODE: 97639328)
> Try this quiz out after you review all the topics!


<style>
        /* Modal container */
        .modal {
            display: none; /* Hidden by default */
            position: fixed;
            z-index: 1; /* On top */
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8); /* Black background with opacity */
        }

        /* Modal content */
        .modal-content {
            position: relative;
            background-color: white;
            margin: auto;
            padding: 20px;
            width: 90%; /* Modal size almost full screen */
            height: 90%; /* Modal height */
            border-radius: 10px;
            overflow: hidden; /* Hide overflow */
        }

        /* Close button */
        .close {
            position: absolute;
            top: 10px;
            right: 20px;
            color: black;
            font-size: 30px;
            font-weight: bold;
            cursor: pointer;
        }

        /* Embed content */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
</style>

<button id="openModal">Open Modal</button>

<!-- The Modal -->
<div id="myModal" class="modal">

<!-- Modal content -->
<div class="modal-content">
    <span class="close">&times;</span>
    <!-- Embedded content (YouTube video in this example) -->
    <embed src="https://quizizz.com/join" width="1000px" height="600px">
</div>

</div>

<script>
    // Get modal and elements
    const modal = document.getElementById("myModal");
    const btn = document.getElementById("openModal");
    const span = document.getElementsByClassName("close")[0];

    // Open modal on button click
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Close modal when 'x' is clicked
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Close modal when clicking outside the modal content
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
</script>

## Popcorn Hack #1
> Please abstract the keys of bananas, apples, and pears, and assign them to numbers 1, 2, and 3 in the most effective way possible.
> Please print out the output of access one values through its corresponding key.

<details>
    <summary>See Answer</summary>
    <pre><code>
bestDictionaryEver = {"bananas": 1, "apples": 2, "pears": 3}
print(bestDictionaryEver["pears"]) #any key will do
    </code></pre>
</details>

## Popcorn Hack #2
> Please create a simple calculator in JavaScript and python, with only the basic functions of division, addition, subtraction, and multiplication.
> You do not need to build an interface for the calculator, it can be completely command line based.
> For example, first input = first number, second input = second number, and third input = math function.

<details>
    <summary>See Answer</summary>
    <pre><code>
firstNumber = int(input("Please Enter the First Number Here: "))
secondNumber = int(input("Please Enter the Second Number Here: "))
mathFunction = int(input("Please Enter the function here: ")) #Ex: +, -, *, /

if mathFunction == "+":
    print(firstNumber + secondNumber)
elif mathFunction == "-":
    print(firstNumber - secondNumber)
elif mathFunction == "*":
    print(firstNumber * secondNumber)
elif mathFunction == "/":
    print(firstNumber / secondNumber)
    </code></pre>
</details>

## Popcorn Hack #3

> Task: Write a function that takes a list of strings and an integer n. The function should return a new list where each > string in the original list is repeated n times.

<details>
    <summary>See Answer</summary>
    <pre><code>
def repeat_strings_in_list(strings, n): 
    result = [] # Creating array
    for string in strings:
        result.append(string * n)  # Repeating the string `n` times
    return result

string_list = ["hello", "world", "python"]
print(repeat_strings_in_list(string_list, 3))
    </code></pre>
</details>


## Popcorn Hack #4

> Please create a function that compares two sets, and checks if there is an value within set 2 that is within set 1. If a value from set 2 is in set 1, then return the boolean output 'True' . If not, then return the boolean value 'False'. Here is an example of a check for your code:


```python
print(sets_have_common_elements({1, 2, 3}, {3, 4}))  # Output: True
print(sets_have_common_elements({1, 2, 3}, {4, 5}))  # Output: False
```

<details>
    <summary>See Answer</summary>
    <pre><code>
def sets_have_common_elements(set1, set2):
    for elem in set1:
        if elem in set2:
            return True
    return False
print(sets_have_common_elements({1, 2, 3}, {3, 4}))  # Output: True
print(sets_have_common_elements({1, 2, 3}, {4, 5}))  # Output: False
print(sets_have_common_elements({1, 2}, {2}))         # Output: False
print(sets_have_common_elements({}, {}))             # Output: False
    </code></pre>
</details>


## Homework Hack

### Part 1: Create a Profile Information (dict)
Create a dictionary called "profile" that contains the following keys.
Create the variables "name", "age", "city", and "favorite_color".
Assign values to these keys. Name should be a string, age should be an integer, city should be a string, and favorite_color should be a string.

<details>
    <summary>See Answer</summary>
    <pre><code>
profile = {
    "name": "Your Name",
    "age": 15,
    "city": "Your City",
    "favorite_color": "Blue"
}
print("Profile:", profile)
    </code></pre>
</details>


### Part 2: Create a List of Hobbies (list)
Create a list called "hobbies" that includes three of your hobbies as strings. Print the "hobbies" list.

<details>
    <summary>See Answer</summary>
    <pre><code>
hobbies = ["Reading", "Gaming", "Swimming"]
print("Hobbies:", hobbies)
    </code></pre>
</details>


### Part 3: Add Hobbies to Profile (dict and list)
Add the "hobbies" list to the "profile" dictionary under the key "hobbies". Print the updated "profile" dictionary.

<details>
    <summary>See Answer</summary>
    <pre><code>
profile["hobbies"] = hobbies
print("Updated Profile:", profile)
    </code></pre>
</details>


### Part 4: Check Availability of a Hobby (bool)
Choose one of your hobbies and create a boolean variable called "has_hobby". Set "has_hobby" to True if your hobby is available to do today, otherwise set it to False. Print a message using "has_hobby" like: "Is <<your hobby>> available today? <<True/False>>"

<details>
    <summary>See Answer</summary>
    <pre><code>
has_hobby = True  # or False
print(f"Is {hobbies[0]} available today? {has_hobby}")
    </code></pre>
</details>


### Part 5: Total Number of Hobbies (int)
Create a variable called "total_hobbies" and set it to the number of hobbies in your "hobbies" list. Print a message like: "I have <<total_hobbies>> hobbies."

<details>
    <summary>See Answer</summary>
    <pre><code>
total_hobbies = len(hobbies)
print(f"I have {total_hobbies} hobbies.")
    </code></pre>
</details>


### Part 6: Favorite Hobbies (tuple)
Create a tuple called "favorite_hobbies" that contains your two most favorite hobbies. Print the "favorite_hobbies" tuple.

<details>
    <summary>See Answer</summary>
    <pre><code>
favorite_hobbies = ("Gaming", "Reading")
print("Favorite Hobbies:", favorite_hobbies)
    </code></pre>
</details>


### Part 7: Add a New Item to Your Profile (set)
Create a set called "skills" and add three unique skills you have. Print the set of "skills".

<details>
    <summary>See Answer</summary>
    <pre><code>
skills = {"Coding", "Drawing", "Cooking"}
print("Skills:", skills)
    </code></pre>
</details>


### Part 8: Decide to Add a New Skill (NoneType)
You are thinking about learning a new skill. Create a variable called "new_skill" and set it to None (you haven't decided yet). Print the value of "new_skill".


<details>
    <summary>See Answer</summary>
    <pre><code>
new_skill = None
print("New Skill:", new_skill)
    </code></pre>
</details>


### Part 9: Calculate Total Profile Cost (float)
Assume each hobby costs $5 to pursue and each skill costs $10 to develop. Create a variable called "total_cost" as a float, and calculate how much it would cost to develop all your hobbies and skills. Print the total cost.

<details>
    <summary>See Answer</summary>
    <pre><code>
total_cost = float(total_hobbies * 5 + len(skills) * 10)
print(f"Total cost to pursue hobbies and skills: ${total_cost:.2f}")
    </code></pre>
</details>


## BONUS: Remake the entire thing using JavaScript!


