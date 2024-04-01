from ninja import Schema

class MovieSchema(Schema):
    name: str
    protagonists: str = None
    poster: str
    trailer: str
    start_date: str  # Change to DateTimeField in models.py if needed
    status: str
    ranking: int

class MovieListSchema(Schema):
    results: list[MovieSchema]

class MovieCreateSchema(Schema):
    data: MovieSchema
