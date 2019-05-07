# 迭代,T(n)=O(n),S(n)=O(1)
def max_iterate(list_=None):
    if list_ is None:
        list_ = []
    for num in list_:
        if num > list_[0]:
            list_[0] = num
    return list_[0]


# 递归,T(n)=O(lgn),S(n)=O(lgn)
def max_recursive(left, right, list_=None):
    if list_ is None:
        list_ = []

    if left + 1 == right:
        return max(list_[left], list_[right])
    else:
        key = (left + right) // 2
        return max(max_recursive(left, key, list_), max_recursive(key, right, list_))
