text = input("Text: ")
words = text.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

max_length = max(len(word) for word in words)

for word, count in counts.items():
    print(f"{word:{max_length}}:{count}")