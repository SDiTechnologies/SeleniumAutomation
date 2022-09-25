# automate the boring stuff sample data
formData = [
    {
        "name": "Alice",
        "fear": "eavesdroppers",
        "source": "wand",
        "robocop": 4,
        "comments": "Tell Bob I said hi.",
    },
    {
        "name": "Bob",
        "fear": "bees",
        "source": "amulet",
        "robocop": 4,
        "comments": "n/a",
    },
    {
        "name": "Carol",
        "fear": "puppets",
        "source": "crystal ball",
        "robocop": 1,
        "comments": "Please take the puppets out of the break room.",
    },
    {
        "name": "Alex Murphy",
        "fear": "ED-209",
        "source": "money",
        "robocop": 5,
        "comments": "Protect the innocent. Serve the public trust. Uphold the law.",
    },
]

keyPresses = {
    "source": {
        "wand": ("down", 1),
        "amulet": ("down", 2),
        "crystal ball": ("down", 3),
        "money": ("down", 4),
    },
    "robocop": {
        1: (" ", 1),
        2: ("right", 1),
        3: ("right", 2),
        4: ("right", 3),
        5: ("right", 4),
    },
}
