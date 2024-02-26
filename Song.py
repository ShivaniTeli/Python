from collections import Counter

total_songs = int(input())
singer_songs = list(map(int, input().split()))
count_singer_songs = Counter(singer_songs)
max_count = max(count_singer_songs.values())
final_count = sum(1 for a in count_singer_songs.values() if a == max_count)
print(final_count)
