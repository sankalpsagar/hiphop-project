import lyricsgenius
genius = lyricsgenius.Genius("9Ut8vL84pWhIkO1CBGuCI9CHdmdrGuQjlYISb4QhNwVLrSlTPc5OFSDReU0I6e8T")

def getLyrics(Song = "Roxanne", Artist= "Arizona Zervas"):
	# artist = genius.search_artist(Artist, max_songs = 1)
	song = genius.search_song(Song, Artist)
	print(song.lyrics)

getLyrics()