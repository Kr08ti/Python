def make_abba(a , b):
    print a + b + b + a
make_abba('Hi', 'Bye')


def hello_name(name):
    print 'Hello' +' '+ name + '!'
hello_name('xyz')


def string_times(str, n):
  if n == 0:
    print n
  for i in range(n):
    print (str*n)
string_times('Hi', 0)