def word_search(matrix, word):
    length = len(matrix[0])
    for i in range(len(matrix)):
        words = ''.join(matrix[i])
        if word in words:
            return True

    for i in range(length):
        temp = []
        for j in matrix:
            temp.append(j[i])
        words = ''.join(temp)
        if word in words:
            return True
    return False


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'IPBS'))
