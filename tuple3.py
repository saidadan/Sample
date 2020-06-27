imelda = "More Mayhem", "Imelda May", 2011, [
    (1, "Pulling the Rug"), (2, "pyscho"), (3, "Mayhem"), (4,"Kentish Town Waltz")]
print(imelda)

imelda[3].append((5, "All for you"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    # print("\t", song)
    track, titles = song
    print("\t Track number {}, Title: {}".format(track, titles))
