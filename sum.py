# divide and conquer
def sum(low, high, list_=None):
    if list_ is None:
        list_ = []
    if low == high:
        return list_[low]
    mid = (low + high) >> 1
    return sum(low, mid, list_) + sum(mid + 1, high, list_)
