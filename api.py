def log_request_response(func):
    def wrapper(self, req, res):
        print("Request received")
        result = func(self, req, res)   # call the original function
        print("Response sent")
        return result
    return wrapper

def log_request_response2(func):
    def wrapper(self, req, res):
        print("Request received 2")
        result = func(self, req, res)   # call the original function
        print("Response sent 2")
        return result
    return wrapper


class RestApi:

    @log_request_response
    @log_request_response2
    def post(self, request, response):
        return "this is a post method"


r = RestApi()
print(r.post({"name": "rohan"}, {}))


