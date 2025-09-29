def h(x): return x 

class E:
  def id(self, v):
    return v

class D: 
  def id(self, v):
    return v

class C: 
  def id(self, v): 
    return v

class B:
  def g(self):     
    c = C()        
    s = D()        
    t = E()        
    d = c.id(s)
    d.id(1) # insens: D.id, E.id
    e = c.id(t)

class A:
  def f(self):     
    b = B()        
    temp1 = b.g()          
    temp2 = b.g()          

a = A()
temp3 = a.f()
temp4 = h(a)

