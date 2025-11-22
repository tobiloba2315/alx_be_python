def get_weather():
    return input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

def advice_for(weather):
    if weather == 'sunny':
        return " Wear a t-shirt and sunglasses."
    elif weather == 'rainy':
        return "Don't forget your umbrella and a raincoat."
    elif weather == 'cold':
        return " Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    weather = get_weather()
    print(advice_for(weather))

if __name__ == '__main__':
    main()
