# CUSTOM MODLES
from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flowe = "Sunflower"

song = "Home on the Range"


def randomfact():
    funfacts = [
        "kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is kansas City.",
        "A considerable portion of kansas City is actually in Missouri.",
        "most kansans are annoyed by Wizard of OZ references from people ouside of kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfact()
