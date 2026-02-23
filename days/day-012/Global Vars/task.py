"""
You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

a = 1
def my_function():
    a += 1
    print(a)
But this will work

a = 1
def my_function():
    global a
    a += 1
    print(a)
"""
# How to modify Global Variable

enemies = 5

def increase_enemies():
    global enemies # global keyword allowed us to update global variable inside local scope
    enemies += 3
    print(enemies)

increase_enemies()
print(enemies)

# other way is to use arguments and parameter in function

o_enemies = 5

def o_increase_enemies(o_en):
    o_en += 2
    return o_en

print(o_increase_enemies(o_enemies))