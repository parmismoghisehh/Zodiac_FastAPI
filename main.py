@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "animal": None,
            "year": None,
            "error": None
        }
    )


@app.post("/", response_class=HTMLResponse)
def get_zodiac(request: Request, year: int = Form(...)):

    if year < 1900 or year > 2100:
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "animal": None,
                "year": year,
                "error": "Please enter a year between 1900 and 2100."
            }
        )

    animal = calculate_zodiac(year)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "animal": animal,
            "year": year,
            "error": None
        }
    )