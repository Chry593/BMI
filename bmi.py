# -*- coding: utf-8 -*-
"""
BMI CALCULATOR
"""
def bmi():
    weight = int(input("Insert your weight (kg): "))
    height = int(input("Insert you height  (cm): "))
    height = float(height / 100)
    bmi = float(weight / (height*height))
    
    if bmi < 18.5:
        print("Under weight")
    elif 18.5 <= bmi <= 29.9:
        print("Normal")
    elif 30.0 <= bmi <=34.9:
        print("Obese")
    elif bmi >= 35:
        print("Extremely obese")

    print("Your Body Mass Index is: {:.2f}".format(bmi))
