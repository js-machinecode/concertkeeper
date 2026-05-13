from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ConcertKeeper"}

@app.get("/concerts")
def get_concerts():
    return [
        {
            "id": 1,
            "artist_name": "Metallica",
            "concert_date": "2026-08-14",
            "venue_name": "Madison Square Garden",
            "city": "New York",
            "state": "NY",
            "status": "upcoming",
            "notes": "First concert saved in ConcertKeeper.",
            "setlist": [],
            "merch_purchased": False,
            "attendance_estimate": 20000
        }
    ]