import grequests

class Test:
    def __init__(self):
        self.urls = [
            'http://www.example.com',
            'http://www.google.com', 
            'http://www.yahoo.com',
            'http://www.stackoverflow.com/',
            'http://www.reddit.com/'
        ]

    def exception(self, request, exception):
        print("Problem: {}: {}".format(request.url, exception))

    def async_req(self):
        results = grequests.map((grequests.get(u) for u in self.urls), exception_handler=self.exception, size=5)
        return results

test = Test()
test.async_req()