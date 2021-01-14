import sys

modname = "module2"
module2 = __import__(modname)
print(module2)

print("module2.x:", module2.x)
print("module2.__dict__['x']:", module2.__dict__['x'])
print("sys.modules['module2'].x:", sys.modules['module2'].x)
print("getattr(module2, 'x'):", getattr(module2, 'x') )
