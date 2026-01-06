# Same example as above, but without the nonlocal keyword:

def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


# Make a function inside a function, which uses the variable x as a non local variable:

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

