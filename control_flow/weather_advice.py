#!/usr/bin/env python3
def get_weather():
    choices = ("sunny", "rainy", "cold")
    prompt = f"Enter current weather ({', '.join(choices)}): "
    while True:
        weather = input(prompt).strip().lower()
        if weather in choices:
            return weather
        print("Invalid input. Please enter: sunny, rainy, or cold.")

if __name__ == "__main__":
    weather = get_weather()
    print(weather)
    prompt = "What's the weather like today? (sunny/rainy/cold) "
    choices = ("sunny", "rainy", "cold")

    while True:
        weather = input(prompt).strip().lower()
        if weather in choices:
            break
        print("Invalid input. Please enter: sunny, rainy, or cold.")

       
    if weather == "sunny":
                    print("Wear a t-shirt and sunglasses")
    elif weather == "rainy":
                    print("Don't forget your umbrella and a raincoat")
    elif weather == "cold":
                    print("Wear a warm jacket and a scarf")
    else:
                    print("Sorry, I don't have recommendations for this weather")
            