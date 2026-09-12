def word_count(text):
    return len(text.split())
def character_count(text):
    return len(text)
def sentence_count(text):
    return len(text.split(".")) - 1
def unique_word_count(text):
    words = text.lower().split()
    return len(set(words))
def most_common_word(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return max(word_counts, key=word_counts.get)