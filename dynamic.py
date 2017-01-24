price_to_length = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30,
}

from collections import defaultdict


def bottom_up_cut_rod(price_listing, rod_length):
    # print price_listing, "THIS IS PRICE LISTING"
    revenue = defaultdict(list)
    revenue[0] = 0
    # j = 0 because no revenue
    for j in range(1, rod_length + 1):
        # print "THIS IS J", j
        q = 0
        for i in range(1, j+1):
            # print "THIS IS I", i
            # print "THIS IS REVENUE", revenue
            q = max(q, price_listing[i] + revenue[j - i])
            # print "THIS IS THE SECOND PART", price_listing[i]
            # print "REV [j-i]", revenue[j-i]
            # print "THIS IS q", q
        revenue[j] = q
    return revenue[rod_length]


def extended_bottom_up_cut_rod(price_listing, rod_length):
    revenue = defaultdict(list)
    size = defaultdict(list)
    revenue[0] = 0
    for j in range(1, rod_length + 1):
        q = 0
        for i in range(1, j+1):
            if q < price_listing[i] + revenue[j - i]:
                q = price_listing[i] + revenue[j - i]
                size[j] = i
        revenue[j] = q
    return revenue[rod_length], size[rod_length]

print extended_bottom_up_cut_rod(price_to_length, 10)
print extended_bottom_up_cut_rod(price_to_length, 6)


def largest_sum(nums):
    """
    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

    >>> largest_sum([2, 2, -10, 1, 5, -20, 5])
    [1, 5]

    """
    # Our best (update as we find new bests)
    best_sum = 0
    start_of_best = 0
    end_of_best = -1  # (nothing)

    # Current sum and start
    current_sum = 0
    start_of_curr = 0

    for i, n in enumerate(nums):
        current_sum += n

        if current_sum > best_sum:
            # Best so far -- record this sum & its start and end
            best_sum = current_sum
            start_of_best = start_of_curr
            end_of_best = i

        if current_sum <= 0:
            # Dropped belonw 1, so we can't improve -- reset
            # start_of_best, to begin with next number
            start_of_curr = i + 1
            current_sum = 0

    return nums[start_of_best:end_of_best + 1]


START = {
    0: -1,
    1: 1,
    2: 3,
    3: 0,
    4: 5,
    5: 3,
    6: 5,
    7: 6,
    8: 8,
    9: 8,
    10: 2,
    11: 12,
}

END = {
    0: 0,
    1: 4,
    2: 5,
    3: 6,
    4: 7,
    5: 9,
    6: 9,
    7: 10,
    8: 11,
    9: 12,
    10: 14,
    11: 16,
}


def recurisive_activity_selector(start_time, finish_time, k, size):
    m = k + 1
    while m <= size and start_time[m] < finish_time[k]:
        m = m + 1
    if m <= size:
        print "first m", m
        result = recurisive_activity_selector(start_time, finish_time, m, size)
        result.insert(0, m)
        print "second m", m
        print "result!!!!!!!!!!", result
        return result
    else:
        return []


print recurisive_activity_selector(START, END, 0, 11)
