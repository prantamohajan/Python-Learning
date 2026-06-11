# Python Local Scope

# a = 40    #Global  scope
# b = 60

# def pm():
#           x = 100    #Local  scope
#           print(x)
# pm()

# print(a)

# Global Keyword .global variable transfer the local variable.

A = 20
B = 200
def myfun ():
          global B
          B = 2000
          print(B)
myfun()

# Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())