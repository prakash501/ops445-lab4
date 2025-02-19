#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    return list(set(l1) |set(l2))

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return sorted(set(l1) & set(l2))

def diff_lists(l1, l2):
    set1, set2 = set(l1), set(l2)
    diff_result = list(set1 ^ set2)  # Remove sorting

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Symmetric Difference: {diff_result}")

    return diff_result  # Unsorted output


if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
