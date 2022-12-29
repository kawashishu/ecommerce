import multiprocessing
import requests

def send_request():
    # Send a request to your Django application
    response = requests.get('http://localhost:8000')
    print(response.status_code)


def __main__():
    # Create 10 processes that execute the send_request function
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=send_request)
        processes.append(p)
        p.start()

if __name__ == '__main__':
    __main__()

