## Python Class Variable vs. Instance Variable: What’s the Difference?

A Python class attribute is an attribute of the class rather than an attribute of an instance of a class.

```python
class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var
```

Note that all instances of the class have access to class_var, and that it can also be accessed as property of the class itself.

```bash
>>> from main import MyClass
>>> foo = MyClass(2)
>>> bar = MyClass(3)
>>> foo.class_var, foo.i_var
(1, 2)
>>> bar.class_var, bar.i_var
(1, 3)
>>> MyClass.class_var
1
```

Python classes and instances of classes each have their own distinct namespaces represented by pre-defined attributes MyClass.__dict__ and instance_of_MyClass.__dict__, respectively.

When you try to access an attribute from an instance from an instance of a class, it first looks at its instance namespace. If it finds the attribute, it returns the attribute.

The instance namespace takes supremacy over the class namespace: if there is an attribute with the same name in both, the instance namespace will be checked first and its value returned.

## How Class Attributes Handle Assingment
With this in mind, we can make sense of how pytho class attributes handle assingnment:

- If a class attribut is set by accessing the class, it will override the value for all instances.

```bash
>>> foo = MyClass(2)
>>> foo.class_var
1
>>> MyClass.class_var = 2
>>> foo.class_var
2
>>> 
```

- If a python class variable is se by accessing an instance, it will override the value only for that instance. This essentially overrides the class variable and turns it into an instance variable available, intuitively, only for that instance.

```bash
>>> foo.class_var
2
>>> MyClass.class_var
2
>>> foo.__dict__
{'i_var': 2}
>>> foo.class_var = 4
>>> foo.class_var
4
>>> MyClass.class_var
2
>>> foo.__dict__
{'i_var': 2, 'class_var': 4}
>>> 
```