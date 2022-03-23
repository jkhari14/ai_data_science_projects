#import sys
import collections

output_file = open(f"Q1c0.txt", "w")
cnt = collections.Counter()
for i in range(2011, 2022):
    input_file = open(f'data4{i}.txt')
    output_file.write(f"{i}:")
    output_file.write('\n')
    for key_word in input_file:
        cnt[key_word] += 1
    for key in cnt.most_common(10):
        output_file.write(f"{key[0].strip()}, {key[1]}")
        output_file.write('\n')
    output_file.write('\n')
