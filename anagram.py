import time


def checkoff(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    list_b = list(str_b)
    for char in str_a:
        if char in list_b:
            list_b.remove(char)
        else:
            return False
    if not list_b:
        return True


def count_and_compare(str_a, str_b):
    count_a = [0] * 26
    count_b = [0] * 26
    for char in str_a:
        count_a[ord(char)-ord('a')] += 1
    for char in str_b:
        count_b[ord(char)-ord('a')] += 1

    if count_a != count_b:
        return False
    return True


s1 = 'abc'
s2 = 'bca'
s3 = 'adc'

start = time.time()
print(checkoff(s1, s2))
end = time.time()
print(count_and_compare(s1, s2))
new_end = time.time()
print("time costs: %f" % (end-start))
print("time costs: %f" % (new_end-end))

s4 = list(s3)
reversed(s4)
print(s4)
