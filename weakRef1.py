import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
        def repr(self):
            return str(self.value)
a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print(d['primary'])         # fetch the object if it is still alive
print(d)
print(d['primary'].value)
del a                       # remove the one reference
print(gc.collect())         # run garbage collection right away
d['primary']                # entry was automatically removed