#Build a temperature converter CLI tool

import argparse

def tempconverter(args):
    unit = args.unit.lower()

    if unit == 'c':
        c_to_f = (args.temperature*(9/5))+32
        c_to_k = args.temperature+273.15
        print(f"Fahrenheit = {round(c_to_f,2)}°F,Kelvin = {round(c_to_k, 2)}k")
    elif unit == "f":
        f_to_c = (args.temperature-32)*(5/9)
        f_to_k = (args.temperature-32)*(5/9)+273.15
        print(f"Celsius = {round(f_to_c, 2)}°C, Fahrenheit = {round(f_to_k,2)}K")
    elif unit == 'k':
        k_to_c = args.temperature-273.15
        k_to_f = (args.temperature-273.15)*(9/5)+32
        print(f"Celsius = {round(k_to_c,2)}°C, Fahrenheit = {round(k_to_f, 2)}°F")
    else:
        print("enter temperature within three units: Celsius , Fehrenheit, kelvin")

parser = argparse.ArgumentParser()
parser.add_argument("temperature", help = "display a temperature", type = int)
parser.add_argument("unit", help = "display a unit")
args = parser.parse_args()

tempconverter(args)




