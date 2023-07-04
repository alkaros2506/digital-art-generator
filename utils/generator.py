import time
import requests
import random
import openai

from utils.helpers import file_path


def generate_img_url(prompt: str) -> str:
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    return response["data"][0]["url"]


def generate_prompt() -> str:
    """
    This function generates a prompt for the OpenAI API.
    The logic is as follows:
    - Choose a random style from the list of styles
    - Choose a random artist from the list of artists
    - Choose a random theme from the list of themes
    - Choose a random protagonist from the list of protagonists
    """
    styles = [
        "anime",
        "abstract",
        "art nouveau",
        "baroque",
        "cubism",
        "dada",
        "digital art",
        "modern art",
        "sculpture",
        "expressionism",
        "impressionism",
        "minimalism",
        "modernism",
        "pop art",
        "post-impressionism",
        "realism",
        "renaissance",
        "rococo",
        "romanticism",
        "surrealism",
        "grafitti",
    ]

    themes = [
        "nature",
        "love",
        "death",
        "war",
        "religion",
        "politics",
        "science",
        "technology",
        "history",
        "philosophy",
        "culture",
        "psychology",
        "society",
        "space",
    ]

    protagonists = [
        "dog",
        "pirate",
        "robot",
        "astronaut",
        "wizard",
        "witch",
        "vampire",
        "ghost",
        "diver",
        "submarine",
        "dragon",
        "baby",
        "child",
        "sailing boat",
        "elephant",
        "girrafe",
        "tiger",
        "lion",
        "construction worker",
        "firefighter",
        "police officer",
        "doctor",
    ]

    artists = [
        "Leonardo da Vinci",
        "Vincent van Gogh",
        "Pablo Picasso",
        "Claude Monet",
        "Michelangelo",
        "Rembrandt",
        "Jackson Pollock",
        "Andy Warhol",
        "Edvard Munch",
        "Salvador Dali",
        "Henri Matisse",
        "Paul Cezanne",
        "Raphael",
        "Banksy",
        "Frida Kahlo",
        "Hopare",
    ]

    style = random.choice(styles)
    artist = random.choice(artists)
    theme = random.choice(themes)
    protagonist = random.choice(protagonists)

    prompt = f"""
    This is an art piece of {protagonist} in the style of {style} by {artist}.
    This art piece is about {theme}.
    """

    print(prompt)

    return prompt


def download_img(url: str, img_index) -> str:
    """
    This function downloads an image from a given url.
    """
    # encode url to be filename friendly (remove special characters)
    filename = file_path(f"image-{img_index}-{time.time()}.png")
    with open(filename, "wb") as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    return filename


def get_n_images(n=4) -> list[any]:
    """
    This function generates n images using the OpenAI API.
    """
    images = []
    for i in range(n):
        prompt = generate_prompt()
        img_url = generate_img_url(prompt)
        images.append(
            {
                "url": img_url,
                "prompt": prompt,
                "src": "openai",
                "filename": download_img(img_url, i),
            }
        )
    return images
