def movie_schema(movie) -> dict:
    return {
        "idMovie": str(movie["_id"]),
        "title": movie["title"],
        "year": movie["year"],
        "category": movie["category"]
    }