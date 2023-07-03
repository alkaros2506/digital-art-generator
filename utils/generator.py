import time
import requests

from io import BytesIO
import random
from PIL import Image

from typing import Any
import openai


def generate_img_url(prompt: str) -> str:
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
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
        "abstract expressionism",
        "art nouveau",
        "baroque",
        "cubism",
        "dada",
        "expressionism",
        "fauvism",
        "impressionism",
        "minimalism",
        "modernism",
        "pointillism",
        "pop art",
        "post-impressionism",
        "realism",
        "renaissance",
        "rococo",
        "romanticism",
        "surrealism",
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
        "woman",
        "man",
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
    ]

    # 15 unique and very famous artists
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
        "Gustav Klimt",
        "Paul Gauguin",
    ]

    style = random.choice(styles)
    artist = random.choice(artists)
    theme = random.choice(themes)
    protagonist = random.choice(protagonists)

    prompt = f"""
    This is an art piece of {protagonist} in the style of {style} by {artist}.
    The painting is about {theme}.
    """

    print(prompt)

    return prompt


def download_img(url: str, img_index) -> str:
    """
    This function downloads an image from a given url.
    """
    # encode url to be filename friendly (remove special characters)
    filename = f"/Users/alkis/Desktop/image-{img_index}-{time.time()}.png"
    with open(filename, "wb") as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    return filename


def get_n_images(n=4) -> list[Any]:
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


if __name__ == "__main__":
    get_n_images(3)
