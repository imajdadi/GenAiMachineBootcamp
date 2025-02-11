#Create a dictionary by using all the given variables.

dictionary = {

'first_name' : 'John',
'last_name' : 'Doe',
'favorite_hobby' :'Python',
'sports_hobby' : 'gym',
'age' : 82 
}
print(dictionary)
#Print the total duration of the playlist
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}
for song in playlist['songs']:
    print(f"Duration : {song['duration']} minutes")

# Calcul de la durée totale
total_duration = sum(song['duration'] for song in playlist['songs'])
print(f"Total duration of the playlist: {total_duration} minutes")