"""
Vasya works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance.
 Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song,
Vasya inserts a certain number of words "WUB" before the first word of the song (the number may be zero),
after the last word (the number may be zero),
and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words,
including "WUB", in one string and plays the song at the club.

For example,
a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Petya has heard Vasya's new dubstep track, but since he isn't into modern music,
 he decided to find out what was the initial song that Vasya remixed. Help Petya restore the original song.
"""


def dubstep(song):
    i = 0
    j = len(song) - 1
    while song[i] == 'W' and song[i + 1] == 'U' and song[i + 2] == 'B' and i < j:
        i += 3
    while song[j - 2] == 'W' and song[j - 1] == 'U' and song[j] == 'B' and i < j:
        j -= 3
    while i <= j:
        if song[i] == 'W' and song[i + 1] == 'U' and song[i + 2] == 'B':
            print(" ", end='')
            while song[i] == 'W' and song[i + 1] == 'U' and song[i + 2] == 'B':
                i += 3
        else:
            print(song[i], end='')
            i += 1


song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
dubstep(song)


"""
Độ phức tạp:....
"""