from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Chinese Zodiac API",
    description="Returns the Chinese zodiac animal for a given birth year.",
    version="1.0.0"
)

zodiac_animals = [
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig"
]


@app.get("/")
def home():
    return {
        "message": "Welcome to the Chinese Zodiac API",
        "usage": "/zodiac/{year}"
    }


@app.get("/zodiac/{year}")
def get_zodiac(year: int):
    if year < 1900 or year > 2100:
        raise HTTPException(
            status_code=400,
            detail="Year must be between 1900 and 2100."
        )

    index = (year - 4) % 12
    animal = zodiac_animals[index]

    return {
        "year": year,
        "animal": animal
    }