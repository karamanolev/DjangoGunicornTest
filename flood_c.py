import itertools
import threading

import requests

counter = itertools.count()


def poller():
    while True:
        resp = requests.post('http://localhost:8008/c')
        if resp.status_code != 200:
            print('FUCKING HELLLL {}'.format(resp.status_code))
        i = next(counter)
        if i % 50 == 0:
            print(i)


t = [threading.Thread(target=poller) for _ in range(4)]
[i.start() for i in t]
[i.join() for i in t]
