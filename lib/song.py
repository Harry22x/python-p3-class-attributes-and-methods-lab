class Song:
    pass
    count = 0
    genres = []
    artists = []
    genre_count={}
    artist_count={}
    def __init__(self,name,artist,genre):
        pass
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increase_song_count()
        self.add_genre(self.genre)
        self.add_artist(self.artist)
        
    @classmethod
    def increase_song_count(cls,increment =1 ):
        cls.count += increment

    @classmethod
    def add_genre(cls,genre):
        pass
        cls.genres.append(genre)
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
             cls.genre_count[genre] = 1

    @classmethod
    def add_artist(cls,artist):
        cls.artists.append(artist)
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
             cls.artist_count[artist] = 1


    
    