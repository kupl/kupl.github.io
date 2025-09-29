class E:
  pass
class D:
  pass 
class C: 
  def id(self, v): return v

def h(x): return x 

class B:
  def g(self):
    c = C()
    d = h(c.id(D(), E()))
    e = c.id(E())
    print(d, e)

class A:
  def f(self):
    b = B()
    b.g()
    b.g()

a = A()
a.f(1)