################## COMMAND LINE ARGUMENTS #######################

def hello(name, lang):
    greetings = {
        "english": "Hello",
        "spanish": "Hola",
        "french": "Bonjour",
        "german": "Hallo",
        "italian": "Ciao",
        "japanese": "Konnichiwa",
        "korean": "Annyeonghaseyo",
        "russian": "Zdravstvuyte",
    }
    msg = f"{greetings[lang]}, {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse

parser = argparse.ArgumentParser(
    description='Say hello to someone.'
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the person to greet."
)

parser.add_argument(
    "-l", "--lang", metavar="language",
    required=True, choices=[
        "English", "spanish",
        "french", "german",
        "italian", "japanese",
        "korean", "russian"
    ], help="The language of the greeting."
)
args = parser.parse_args()

hello(args.name, args.lang)

# To call this on the terminal type: python hello_person.py -n "name"
# msg = f"Hello, {args.name}!"
# print(msg)
