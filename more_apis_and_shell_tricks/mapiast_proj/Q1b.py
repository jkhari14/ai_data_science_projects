import sys
import collections

input_file = open(f"{sys.argv[1]}", "r")
cnt = collections.Counter()

for key_word in input_file:
    cnt[key_word] += 1


for key in cnt.most_common(10):
    print(f"{key[0].strip()}, {key[1]}")
