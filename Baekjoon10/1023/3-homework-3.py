genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    songs=len(genre_array)
    album={}
    for i in range(0,songs):
        if genre_array[i] not in album:
            album[genre_array[i]]=[(i,play_array[i])]
        else:
            album[genre_array[i]].append((i,play_array[i]))


    answer=[]
    for i in album:
        max_play=0

        album[i].sort(key=lambda x:x[1],reverse=True)
        print(album[i])
        first=album[i][0]
        second=album[i][1]
        answer.append(first[0])
        answer.append(second[0])

    return answer



print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!