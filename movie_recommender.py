"""
CSCI 1101: Movie Recommender

Recommends movies based on user preferences for genre, mood, and era.
Demonstrates nested dictionary lookups, set membership checks, and input loops.
"""

# List of acceptable inputs for genre, mood, and era.
valid_eras = {"classic", "retro", "modern", "recent"}
valid_genre = {"action", "comedy", "drama", "scifi", "horror"}
valid_moods = {"uplifting", "suspenseful", "emotional", "upbeat", "deep"}

# Movie dictionary for different combinations of era, mood, and genre.
movie_recommendation = {
    'action': {
        'uplifting': {
            'classic': 'Ben-Hur (1959)',
            'retro': 'Die Hard (1988)',
            'modern': 'The Matrix (1999)',
            'recent': 'Mad Max: Fury Road (2015)',
        },
        'suspenseful': {
            'classic': 'Rear Window (1954)',
            'retro': 'The Fugitive (1993)',
            'modern': 'Inception (2010)',
            'recent': 'Tenet (2020)',
        },
        'emotional': {
            'classic': 'The Bridge on the River Kwai (1957)',
            'retro': 'The Rock (1996)',
            'modern': 'Gladiator (2000)',
            'recent': 'Avengers: Endgame (2019)',
        },
        'upbeat': {
            'classic': 'The Great Escape (1963)',
            'retro': 'Lethal Weapon (1987)',
            'modern': 'Iron Man (2008)',
            'recent': 'Guardians of the Galaxy (2014)',
        },
        'deep': {
            'classic': 'The Deer Hunter (1978)',
            'retro': 'The Terminator (1984)',
            'modern': 'Children of Men (2006)',
            'recent': 'Mad Max: Fury Road (2015)',
        },
    },
    'comedy': {
        'uplifting': {
            'classic': 'Some Like It Hot (1959)',
            'retro': 'The Pink Panther (1963)',
            'modern': 'Groundhog Day (1993)',
            'recent': 'Palm Springs (2020)',
        },
        'suspenseful': {
            'classic': 'The Odd Couple (1968)',
            'retro': 'A Fish Called Wanda (1988)',
            'modern': 'The Truman Show (1998)',
            'recent': 'The Farewell (2019)',
        },
        'emotional': {
            'classic': 'Its a Wonderful Life (1946)',
            'retro': 'The Apartment (1960)',
            'modern': 'The Pursuit of Happyness (2006)',
            'recent': 'The Upside (2019)',
        },
        'upbeat': {
            'classic': 'The Philadelphia Story (1940)',
            'retro': 'Airplane! (1980)',
            'modern': 'The Hangover (2009)',
            'recent': 'Crazy Rich Asians (2018)',
        },
        'deep': {
            'classic': 'Harold and Maude (1971)',
            'retro': 'A Serious Man (2009)',
            'modern': 'Eternal Sunshine of the Spotless Mind (2004)',
            'recent': 'Inside Out (2015)',
        },
    },
    'drama': {
        'uplifting': {
            'classic': 'Gone with the Wind (1939)',
            'retro': 'One Flew Over the Cuckoos Nest (1975)',
            'modern': 'Schindlers List (1993)',
            'recent': 'The Trial of the Chicago 7 (2020)',
        },
        'suspenseful': {
            'classic': '12 Angry Men (1957)',
            'retro': 'The Godfather (1972)',
            'modern': 'There Will Be Blood (2007)',
            'recent': 'Prisoners (2013)',
        },
        'emotional': {
            'classic': 'Citizen Kane (1941)',
            'retro': 'The Shawshank Redemption (1994)',
            'modern': 'Forrest Gump (1994)',
            'recent': 'A Star is Born (2018)',
        },
        'upbeat': {
            'classic': 'On the Waterfront (1954)',
            'retro': 'The Social Network (2010)',
            'modern': 'La La Land (2016)',
            'recent': 'The Intern (2015)',
        },
        'deep': {
            'classic': 'The Graduate (1967)',
            'retro': 'Taxi Driver (1976)',
            'modern': 'Requiem for a Dream (2000)',
            'recent': 'The Revenant (2015)',
        },
    },
    'scifi': {
        'uplifting': {
            'classic': 'Metropolis (1927)',
            'retro': 'Star Wars (1977)',
            'modern': 'Minority Report (2002)',
            'recent': 'Dune (2021)',
        },
        'suspenseful': {
            'classic': 'The Day the Earth Stood Still (1951)',
            'retro': 'The Matrix (1999)',
            'modern': 'Blade Runner 2049 (2017)',
            'recent': 'Arrival (2016)',
        },
        'emotional': {
            'classic': '2001: A Space Odyssey (1968)',
            'retro': 'The Terminator (1984)',
            'modern': 'Her (2013)',
            'recent': 'Interstellar (2014)',
        },
        'upbeat': {
            'classic': 'Flash Gordon (1980)',
            'retro': 'Back to the Future (1985)',
            'modern': 'Guardians of the Galaxy (2014)',
            'recent': 'The Martian (2015)',
        },
        'deep': {
            'classic': 'Solaris (1972)',
            'retro': 'The Matrix (1999)',
            'modern': 'Children of Men (2006)',
            'recent': 'Ex Machina (2014)',
        },
    },
    'horror': {
        'uplifting': {
            'classic': 'Psycho (1960)',
            'retro': 'Night of the Living Dead (1968)',
            'modern': 'The Sixth Sense (1999)',
            'recent': 'A Quiet Place (2020)',
        },
        'suspenseful': {
            'classic': 'The Shining (1980)',
            'retro': 'Jaws (1975)',
            'modern': 'Get Out (2017)',
            'recent': 'Hereditary (2018)',
        },
        'emotional': {
            'classic': 'Nosferatu (1922)',
            'retro': 'The Exorcist (1973)',
            'modern': 'The Others (2001)',
            'recent': 'It Follows (2014)',
        },
        'upbeat': {
            'classic': 'Beetlejuice (1988)',
            'retro': 'Evil Dead 2 (1987)',
            'modern': 'Shaun of the Dead (2004)',
            'recent': 'Scary Movie (2000)',
        },
        'deep': {
            'classic': 'Night of the Living Dead (1968)',
            'retro': 'The Thing (1982)',
            'modern': 'It (2017)',
            'recent': 'Midsommar (2019)',
        },
    },
}


def main():
    while True:
        genre = input("What's your favorite genre? (Action, Comedy, Drama, SciFi, Horror): ").strip().lower()
        if genre in valid_genre:
            print("Your chosen genre is " + genre.capitalize())
            break
        else:
            print("You have chosen an invalid genre, please try again.")

    while True:
        mood = input("Whats your favorite mood? (Uplifting, Suspenseful, Emotional, Upbeat, Deep): ").strip().lower()
        if mood in valid_moods:
            print("Your chosen mood is " + mood.capitalize())
            break
        else:
            print("You have chosen an invalid mood, please try again.")

    while True:
        era = input("What era? (Classic, Retro, Modern, Recent): ").strip().lower()
        if era in valid_eras:
            recommendation = movie_recommendation[genre][mood][era]
            print("Based on your preferences, we recommend: " + recommendation)
            break
        else:
            print("You have chosen an invalid era, please try again.")


if __name__ == "__main__":
    main()