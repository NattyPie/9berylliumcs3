zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

birth_year_input = input("Enter your birth year: ")

if not birth_year_input.isdigit():
    print("Invalid input, please enter a valid number.")
else:
    birth_year = int(birth_year_input)

    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
    else:
        index = (birth_year - 1900) % 12
        print("Your Chinese Zodiac Sign is:", zodiac_signs[index])

