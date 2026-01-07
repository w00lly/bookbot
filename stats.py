def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    amount = {}
    characters = text.lower()
    for c in characters:
        if c in amount:
            amount[c] += 1
        else:
            amount[c] = 1
    return amount

def sorted_list(amount):
    sorted_list = [{"char": k, "num": v} for k, v in sorted(amount.items(), key=lambda x: x[1], reverse=True)]
    return sorted_list
