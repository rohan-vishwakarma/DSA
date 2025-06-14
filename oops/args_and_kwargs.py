# # *args
#
# def logs(type, *data):
#     try:
#         log_types = ['info', 'warning', 'error', 'danger']
#         if type not in log_types:
#             raise ValueError(f"Log Type : {type} Is Not Valid")
#
#         print(f"Log level: {type} ", data)
#     except Exception as e:
#         print(e)
#
# def add_all_subject_grades(*info):
#     logs("warning", *info)
#     return sum(info)
#
# # p = add_all_subject_grades(1,2,3,4,5, 7)


# kwargs

def collect_student_info(**kwargs):
    allowed_fields = ['name', 'age', 'grade']
    validation_error = {'error': {}}
    for i in kwargs.items():
        key , value  = i[0],  i[1]
        if key not in allowed_fields:
            validation_error['error'][f'{key}']=   "Field Not Allowed"
    if len(validation_error) != 0:
        return validation_error
    return kwargs

p1 = collect_student_info(naddme="rohan", ageww="12", gewerade=15)
print(p1)

