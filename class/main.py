class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var


class Service(object):
    data = []

    def __init__(self, other_data):
        self.other_data = other_data


# >>> from main import MyClass
# >>> foo = MyClass(2)
# >>> bar = MyClass(3)
# >>> foo.class_var, foo.i_var
# (1, 2)
# >>> bar.class_var, bar.i_var
# (1, 3)
# >>> MyClass.class_var
# 1