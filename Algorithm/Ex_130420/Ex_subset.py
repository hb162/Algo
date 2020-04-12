"""
The power set of a set is the set of all subsets. Write a function that,
given a set, generates its power set.
"""


def find_subset(my_set):
    output = [[]]
    newsub = []
    for i in my_set:
        for subset in output:
            newsub.append(subset+[i])
        output.extend(newsub)

    return output


print(find_subset({1, 2}))
"""
Độ phức tạp: O(n^2)
"""