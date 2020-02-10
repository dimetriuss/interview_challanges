

def staircase(n: int) -> list:
    if n <= 0 or n > 100:
        raise ValueError("n should be in the range [1; 100]")
    staircase_list = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        shebangs = '#' * i
        staircase_list.append("{}{}".format(spaces, shebangs))
    return staircase_list
