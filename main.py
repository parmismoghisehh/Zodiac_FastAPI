from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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


def calculate_zodiac(year: int):
    index = (year - 4) % 12
    return zodiac_animals[index]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "animal": None,
            "year": None,
            "error": None
        }
    )


@app.post("/", response_class=HTMLResponse)
def get_zodiac(
    request: Request,
    year: int = Form(...)
):
    if year < 1900 or year > 2100:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "animal": None,
                "year": year,
                "error": "Please enter a year between 1900 and 2100."
            }
        )

    animal = calculate_zodiac(year)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "animal": animal,
            "year": year,
            "error": None
        }
    )