def log_request_response(funct):
    def wrapper():
        print("request received for fetching student information")
        response = funct()
        print(f"response received")
        return response
    return wrapper

@log_request_response
def student_information():
    dict = {
        "name" : "rohan",
        "age": 23
    }
    print(dict)
    return dict

response = student_information()
