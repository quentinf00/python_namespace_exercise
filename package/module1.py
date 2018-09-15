CONSTANT = 'CONSTANT'


def my_function():
    return 'my_function'


class MyClass(object):
    my_class_attribute = 'my_class_attribute'
    this_should_stay_the_same = 'this_should_stay_the_same'

    def __init__(self):
        self.my_instance_attribute = 'my_instance_attribute'

    def my_class_method(self):
        return 'my_class_method'

    def this_should_work_the_same(self):
        return 'this_should_work_the_same'

    @staticmethod
    def my_class_static_method():
        return 'my_class_static_method'
