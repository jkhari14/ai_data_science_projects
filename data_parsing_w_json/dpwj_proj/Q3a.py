import collections
import matplotlib.pyplot as plt
top_keyword = []
for year in range(2010, 2020+1):
    input_file = open(f"data4{year}.txt", "r")
    cnt = collections.Counter()
    for key_word in input_file:
        cnt[key_word] += 1
    for key in cnt.most_common(1):
        top_keyword.append((key[0], key[1]))
enter = '\n'
for i in range(11):
    plt.bar(i+1, top_keyword[i][1], label=f"{i+2010}: {top_keyword[i][0].strip(enter)}", width=0.8, bottom=None, align='center', data=None)


plt.xlabel("Keywords")
plt.ylabel("Appearances")
plt.title("Number One Keyword from Each Year")
plt.legend()
plt.savefig("Q3a.pdf")

