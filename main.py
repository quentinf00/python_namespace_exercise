import package
from package import CONSTANT as constant_init_import
from package import my_function as my_function_init_import
from package import MyClass as my_class_init_import
from package import module1
from package.module1 import CONSTANT as constant_module_import
from package.module1 import my_function as my_function_module_import
from package.module1 import MyClass as my_class_module_import


def run():
    print('package.my_function() --> ', package.my_function())
    print('package.CONSTANT --> ', package.CONSTANT)
    print('package.MyClass.my_class_attribute --> ', package.MyClass.my_class_attribute)
    print('package.MyClass().my_instance_attribute --> ', package.MyClass().my_instance_attribute)
    print('package.MyClass().this_should_stay_the_same --> ', package.MyClass().this_should_stay_the_same)
    print('package.MyClass().my_class_method() --> ', package.MyClass().my_class_method())
    print('package.MyClass().this_should_work_the_same() --> ', package.MyClass().this_should_work_the_same())
    print('package.MyClass.my_class_static_method() --> ', package.MyClass.my_class_static_method())
    print()
    print()
    print('module1.my_function() --> ', module1.my_function())
    print('module1.CONSTANT --> ', module1.CONSTANT)
    print('module1.MyClass.my_class_attribute --> ', module1.MyClass.my_class_attribute)
    print('module1.MyClass().my_instance_attribute --> ', module1.MyClass().my_instance_attribute)
    print('module1.MyClass().this_should_stay_the_same --> ', module1.MyClass().this_should_stay_the_same)
    print('module1.MyClass().my_class_method() --> ', module1.MyClass().my_class_method())
    print('module1.MyClass().this_should_work_the_same() --> ', module1.MyClass().this_should_work_the_same())
    print('module1.MyClass.my_class_static_method() --> ', module1.MyClass.my_class_static_method())
    print()
    print()
    print('my_function_init_import() --> ', my_function_init_import())
    print('constant_init_import --> ', constant_init_import)
    print('my_class_init_import.my_class_attribute --> ', my_class_init_import.my_class_attribute)
    print('my_class_init_import().my_instance_attribute --> ', my_class_init_import().my_instance_attribute)
    print('my_class_init_import().this_should_stay_the_same --> ', my_class_init_import().this_should_stay_the_same)
    print('my_class_init_import().my_class_method() --> ', my_class_init_import().my_class_method())
    print('my_class_init_import().this_should_work_the_same() --> ', my_class_init_import().this_should_work_the_same())
    print('my_class_init_import.my_class_static_method() --> ', my_class_init_import.my_class_static_method())
    print()
    print()
    print('my_function_module_import() --> ', my_function_module_import())
    print('constant_module_import --> ', constant_module_import)
    print('my_class_module_import.my_class_attribute --> ', my_class_module_import.my_class_attribute)
    print('my_class_module_import().my_instance_attribute --> ', my_class_module_import().my_instance_attribute)
    print('my_class_module_import().this_should_stay_the_same --> ', my_class_module_import().this_should_stay_the_same)
    print('my_class_module_import().my_class_method() --> ', my_class_module_import().my_class_method())
    print('my_class_module_import().this_should_work_the_same() --> ', my_class_module_import().this_should_work_the_same())
    print('my_class_module_import.my_class_static_method() --> ', my_class_module_import.my_class_static_method())
