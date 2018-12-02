def find_index(name):
    count = 0
    for i in dataset['title']:
        if i == name:
            return count
        count+=1