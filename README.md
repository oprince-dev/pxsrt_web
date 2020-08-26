# PxSrt Web Application

## About
> PxSrt is an application that allows you to sort the pixels in an image of your choosing. 

![Mock Landing Page](src/pxsrt/static/img/mocks/mock-landing.jpg)
![Mock Account Page](src/pxsrt/static/img/mocks/mock-account.jpg)
![Mock Sort](src/pxsrt/static/img/mocks/mock-sort.jpg)
![Mock Design (Adobe XD)](src/pxsrt/static/img/mocks/mock-design.jpg)

## Setup (local)
### Step 1:
```
pip3 install -r requirements.txt
python3 src/run.py
```
### Step 2:
* Browse to localhost:5000 in your browser.

## Features
*Everything is stored on your local machine using SQLAlchemy.*
*Sorted images are saved in static/img/sorts/*
* Create an account
* Upload your favorite images
* Select options (mode, threshold, direction, upper, and reverse)
* Preview the pixels that will be selected
* Sort each row of pixels using the almighty Quick Sort!

## Options
Mode | Description
---- | -----------
Hue | Target pixels based off their hue (HSV)
Saturation | Target pixels based off their saturation (HSV)
Value | Target pixels based off their value (HSV)
Red | Target pixels by the amount of red value (RGB)
Green | Target pixels by the amount of green value (RGB)
Blue | Target pixels by the amount of blue value (RGB)

Threshold | Description
--------- | -----------
0-255 | Slider value from 0 to 255

Direction | Description
--------- | -----------
Horizontal | Sort pixels left to right
Vertical | Sort pixels top to bottom

Upper | Description
----- | -----------
No | Selects the lower value pixels (Darker [Value Mode])
Yes | Selects the higher value pixels (Lighter [Value Mode])

Reverse | Description
------- | -----------
No | Sort pixels left -> right  / top -> bottom
Yes | Sort pixels right -> left  / bottom -> top

## Technologies
![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white)
![JQuery](https://img.shields.io/badge/jquery%20-%230769AD.svg?&style=for-the-badge&logo=jquery&logoColor=white)
* SQLAlchemy
