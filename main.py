from sys import stdout, stdin
import time

text = input("text> ")

stdout.write("\rStarting ...")
time.sleep(3)
stdout.flush()
stdout.write("\r               ")

for i in [3,2,1]:
    stdout.write(f"\r{i}")
    time.sleep(1)
    stdout.flush()

stdout.flush()
stdout.write("\r----------------------")
print(" Start ----------------------")


words = text.split()



start_time = time.time()

in_text = input("start typing: \n> ")

finish_time = time.time()

Time = finish_time - start_time

in_words = in_text.split()

tmp = []
for sth in words:
    if sth != "" and sth != " " and sth != "  " and sth != "   ":
        tmp.append(sth)

words = tmp


tmp = []
for sth in in_words:
    if sth != "" and sth != " " and sth != "  " and sth != "   ":
        tmp.append(sth)

in_words = tmp



corrects = 0
for i in range(len(words)):
    if in_words[i] == words[i]:
        corrects = corrects + 1



print(f"total words: {len(words)}")
print(f"correct words: {corrects}")
print(f"mistakes: {len(words)-corrects}")
print(f"time: {str(Time)[:5]}")
print(f"WpM: {str(corrects*(60/int(Time)))[:5]}")

