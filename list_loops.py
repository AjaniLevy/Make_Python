songs = ["ROCKSTAR", "Do it", "For The Night"]
print({songs[0]}, {songs[2]})
print(songs[1:3])
songs[2] = "So It Goes"
print(songs)
songs.extend(["White America", "NEVER", "Goodbye Yellow Brick Road"])
print(songs)
del songs[2]
for song in songs:
    print(song)

for i in range(len(songs)):
    print(songs[i])

print(songs)

animals = ["Penguin", "Polar Bear", "Iguana"]
animals.append("Monkey")
print(animals[2])
del animals[0]
for i in animals:
    print(i)
