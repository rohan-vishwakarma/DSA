
x = 10

def my_func():
    global x
    x = 5   # modifies global x
    print("Inside function:", x)

my_func()
print("Outside function:", x)
