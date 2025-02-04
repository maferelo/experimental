import time

def background_task(name):
    """ Function that simulates a long-running task """
    time.sleep(10)
    return f'Hello, {name}!'