list1 = [1, 3, 5, 7]
list2 = [8, 2, 7, 4]
removeList = [1, 2, 3, 4, 5]
index1 = 2
index2 = 3
input_list = ['spam', 'SPAM', 'spam', 'spam', 'bacon', 'SPAM']
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
input_list_Tupla = [2, 2, 3, 4, 5, 5, 5, 6, 7, 2]


def odd_even_indexes(list1, list2):
    """
    This functions takes two lists and prints all
    the odd-indexed elements from the first list
    and all the even-indexed elements from the second
    and returns them into a single list.
    Example:
    >>> odd_even_indexes([1, 3, 5, 7], [8, 2, 7, 4])
    [3, 7, 8, 7]
    These docstring examples could also be run to test
    correctnes with:
    >>> import doctest; doctest.testmod()
    """
    list3 = list1[1::2] + list2[0::2]
    return list3


def move_element(removeList, index1, index2):
    """
    This function takes a list and takes the element
    at index1 and moves it to the position of index2.
    If any of the indexes is out of bounds, return the
    original list.
    Example:
    >>> remove_at_and_add_at([1, 2, 3, 4, 5], 2, 3)
    [1, 2, 4, 3, 5]
    """
    try:
        tempo1 = removeList[index1]
        removeList.pop(index1)
        removeList.insert(index2, tempo1)
        return removeList
    except IndexError:
        return removeList

def count_elements(input_list):
    """
    This function recieves a list and returns a
    dictionary with the count of each element.
    DO NOT USE A COUNTER OBJECT.
    Example:
    >>> count_elements([
    'spam',
    'SPAM',
    'spam',
    'spam',
    'bacon',
    'SPAM'
    ])
    {'spam': 3, 'SPAM': 2, 'bacon': 1}
    """
    input_dict = {}
    for element in input_list:
        if element in input_dict:
            input_dict[element] += 1
        else:
            input_dict[element] = 1
    return input_dict


def remove_intersection(set1, set2):
    """
    This function takes two sets, removes the intersection
    from the first set and returns it.
    Example:
    >>> remove_intersection({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7})
    {1, 2}
    """
    set3 = set1 - set2
    return set3

def delete_duplicates_to_tuple(input_list_Tupla):
    """
    This function takes a list and returns the same list
    without duplicates but as a tuple.
    Example:
    >>> delete_duplicates_to_tuple([2, 2, 3, 4, 5, 5, 5, 6, 7, 2])
    [2, 3, 4, 5, 6, 7]
    """
    listWithOutDuplicates = tuple()
    for i in input_list_Tupla:
        if i not in listWithOutDuplicates:
            listWithOutDuplicates += (i,)
    return listWithOutDuplicates


print("odd_even_indexes: ", odd_even_indexes(list1, list2))
print("move_element: ", move_element(removeList, index1, index2))
print("count_elements: ", count_elements(input_list))
print("remove_intersection: ", remove_intersection(set1, set2))
print("delete_duplicates_to_tuple: ", delete_duplicates_to_tuple(input_list_Tupla))
