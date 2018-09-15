import package
from package import CONSTANT as constant_init_import
from package import my_function as func_init_import
from package import MyClass as class_init_import
from package import module1
from package.module1 import CONSTANT as constant_module_import
from package.module1 import my_function as func_module_import
from package.module1 import MyClass as class_module_import


def run():
    print(package.my_function(), '--> mock_1')
    print(package.CONSTANT, '--> mock_1')
    print(package.MyClass.my_class_attribute, '--> mock_1')
    print(package.MyClass().my_instance_attribute, '--> mock_1')
    print(package.MyClass().this_should_stay_the_same, '--> DO NOT MOCK ME')
    print(package.MyClass().my_class_method(), '--> mock_1')
    print(package.MyClass().this_should_work_the_same(), '--> DO NOT MOCK ME')
    print(package.MyClass.my_class_static_method(), '--> mock_1')
    print()
    print()
    print(module1.my_function(), '--> mock_2')
    print(module1.CONSTANT, '--> mock_2')
    print(module1.MyClass.my_class_attribute, '--> mock_2')
    print(module1.MyClass().my_instance_attribute, '--> mock_2')
    print(module1.MyClass().this_should_stay_the_same, '--> DO NOT MOCK ME')
    print(module1.MyClass().my_class_method(), '--> mock_2')
    print(module1.MyClass().this_should_work_the_same(), '--> DO NOT MOCK ME')
    print(module1.MyClass.my_class_static_method(), '--> mock_2')
    print()
    print()
    print(func_init_import(), '--> mock_3')
    print(constant_init_import, '--> mock_3')
    print(class_init_import.my_class_attribute, '--> mock_3')
    print(class_init_import().my_instance_attribute, '--> mock_3')
    print(class_init_import().this_should_stay_the_same, '--> DO NOT MOCK ME')
    print(class_init_import().my_class_method(), '--> mock_3')
    print(class_init_import().this_should_work_the_same(), '--> DO NOT MOCK ME')
    print(class_init_import.my_class_static_method(), '--> mock_3')
    print()
    print()
    print(func_module_import(), '--> mock_4')
    print(constant_module_import, '--> mock_4')
    print(class_module_import.my_class_attribute, '--> mock_4')
    print(class_module_import().my_instance_attribute, '--> mock_4')
    print(class_module_import().this_should_stay_the_same, '--> DO NOT MOCK ME')
    print(class_module_import().my_class_method(), '--> mock_4')
    print(class_module_import().this_should_work_the_same(), '--> DO NOT MOCK ME')
    print(class_module_import.my_class_static_method(), '--> mock_4')
