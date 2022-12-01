"""
map moods to a set of query params
"""
mood_map = {
    "happy": {
        "limit": "1",
        "seed_genres": "dance,groove,happy,party,pop",
        "max_danceability": "0.9",
        "min_danceability": "0.75",
        "max_energy": "0.9",
        "min_energy": "0.75",
    },
    "sad": {
        "limit": "1",
        "seed_genres": "ambient,chill,emo,sad",
        "max_danceability": "0.3",
        "max_energy": "0.3",
    },
    "angry": {
        "limit": "1",
        "seed_genres": "emo,hard-rock,metal,punk,rock",
        "max_danceability": "0.5",
        "max_energy": "0.5",
    },
    "in-love": {
        "limit": "1",
        "seed_genres": "romance,summer,singer-songwriter,pop,indie",
        "max_danceability": "0.75",
        "max_energy": "0.75",
        "min_danceability": "0.5",
        "min_energy": "0.5",
    },
}
