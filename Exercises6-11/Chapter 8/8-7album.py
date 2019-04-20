def make_album(artist, album, tracks=''):
    """Return a dictionary containing an artist and album"""
    artist_album = {'artist': artist.title(), 'album': album.title()}
    if tracks:
        artist_album['tracks'] = tracks
    return artist_album

DT = make_album('dream theater', 'distance over time', '10')
KM = make_album('kamelot', 'the shadow theory')
DL = make_album('delain', 'moonbathers')
print(DT)
print(KM)
print(DL)