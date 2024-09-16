def word_count(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    data = data.lower()
    data = data.split()
    counter = {}
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


if __name__ == "__main__":
    file_path = './P1_data.txt'
    print(word_count(file_path))
