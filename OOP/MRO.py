# MRO stands for Method Resolution Order

class A:
    label = 'FROM CLASS A'
class B(A):
    label = 'FROM CLASS B'
class C(A):
    label = 'FROM CLASS C'

# Give priority to the first parent class.
class D(C, B):
  pass

obj = D()
print(obj.label) #Output: FROM CLASS C