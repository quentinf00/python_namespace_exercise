from unittest.mock import patch

import main
import package
import package.module1
from package import module1, MyClass


@patch('package.CONSTANT')
@patch('package.MyClass')
@patch('package.my_function')
def test_patch_package_should_patch_package_import(*args):
    main.run()


@patch.object(package, 'CONSTANT')
@patch.object(package, 'MyClass')
@patch.object(package, 'my_function')
def test_patch_object_package_should_patch_package_import(*args):
    main.run()


@patch('package.module1.CONSTANT')
@patch('package.module1.MyClass')
@patch('package.module1.my_function')
def test_patch_package_module_should_patch_module_import(*args):
    main.run()


@patch.object(package.module1, 'CONSTANT')
@patch.object(package.module1, 'MyClass')
@patch.object(package.module1, 'my_function')
def test_patch_object_package_module_should_patch_module_import(*args):
    main.run()


@patch.object(module1, 'CONSTANT')
@patch.object(module1, 'MyClass')
@patch.object(module1, 'my_function')
def test_patch_object_module_should_patch_module_import(*args):
    main.run()


@patch.object(MyClass, 'my_class_attribute')
@patch.object(MyClass, 'this_should_stay_the_same')
@patch.object(MyClass, 'my_class_method')
@patch.object(MyClass, 'this_should_work_the_same')
@patch.object(MyClass, 'my_class_static_method')
def test_patch_object_my_class_should_patch_in_any_cases(*args):
    main.run()
