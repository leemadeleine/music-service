"""
map given mood strings to a set of query params used to fetch recommendations
"""
mood_map = {
    "happy": {
        "limit": "1",
        "seed_genres": "happy,dance,party",
        "max_danceability": "0.9",
        "min_danceability": "0.75",
        "max_energy": "0.9",
        "min_energy": "0.75",
    },
    "sad": {
        "limit": "1",
        "seed_genres": "sad",
        "max_danceability": "0.5",
        "max_energy": "0.5",
    },
    "angry": {
        "limit": "1",
        "seed_genres": "hard-rock,metal,punk",
        "max_danceability": "0.75",
        "min_danceability": "0.5",
        "max_energy": "0.8",
        "min_energy": "0.5",
    },
    "in-love": {
        "limit": "1",
        "seed_genres": "romance",
        "max_danceability": "0.75",
        "max_energy": "0.75",
        "min_danceability": "0.5",
        "min_energy": "0.5",
    },
}
