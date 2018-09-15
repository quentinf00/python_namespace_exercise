## Namespace python exercise

### (TLDR:)Exercise instructions:
- You should not patch the `main.run` method itself (ie `main.run = lambda: print(expected output)`)
- Implement the `test_main.set_up_mocks` function so that the `python3 test_main.py` command prints:

```
mock_1 --> mock_1
mock_1 --> mock_1
mock_1 --> mock_1
mock_1 --> mock_1
this_should_stay_the_same --> DO NOT MOCK ME
mock_1 --> mock_1
this_should_work_the_same --> DO NOT MOCK ME
mock_1 --> mock_1


mock_2 --> mock_2
mock_2 --> mock_2
mock_2 --> mock_2
mock_2 --> mock_2
this_should_stay_the_same --> DO NOT MOCK ME
mock_2 --> mock_2
this_should_work_the_same --> DO NOT MOCK ME
mock_2 --> mock_2


mock_3 --> mock_3
mock_3 --> mock_3
mock_3 --> mock_3
mock_3 --> mock_3
this_should_stay_the_same --> DO NOT MOCK ME
mock_3 --> mock_3
this_should_work_the_same --> DO NOT MOCK ME
mock_3 --> mock_3


mock_4 --> mock_4
mock_4 --> mock_4
mock_4 --> mock_4
mock_4 --> mock_4
this_should_stay_the_same --> DO NOT MOCK ME
mock_4 --> mock_4
this_should_work_the_same --> DO NOT MOCK ME
mock_4 --> mock_4

```


**Set Up:**
- I wrote a simple python `package` with one submodule `module1.py`  with different kind of objects:
    - one constant
    - one function
    - one class with
       - two class attribute
       - one instance attribute
       - two method
       - one static method

- I then wrote a `main.py` where I:
   - imported different things:
      - import the package
      - import the submodule
      - import the python objects from the `package/__init__.py` files
      - import the python objects from the `module1.py` files
   - And I printed the results of all the methods and object in the `run()` function of the main module:

- I wrote a `test_main.py` where I execute this function:

I you execute the main.run() with `python3 test_main.py` :

```
my_function --> mock_1
CONSTANT --> mock_1
my_class_attribute --> mock_1
my_instance_attribute --> mock_1
this_should_stay_the_same --> DO NOT MOCK ME
my_class_method --> mock_1
this_should_work_the_same --> DO NOT MOCK ME
my_class_static_method --> mock_1


my_function --> mock_2
CONSTANT --> mock_2
my_class_attribute --> mock_2
my_instance_attribute --> mock_2
this_should_stay_the_same --> DO NOT MOCK ME
my_class_method --> mock_2
this_should_work_the_same --> DO NOT MOCK ME
my_class_static_method --> mock_2


my_function --> mock_3
CONSTANT --> mock_3
my_class_attribute --> mock_3
my_instance_attribute --> mock_3
this_should_stay_the_same --> DO NOT MOCK ME
my_class_method --> mock_3
this_should_work_the_same --> DO NOT MOCK ME
my_class_static_method --> mock_3


my_function --> mock_4
CONSTANT --> mock_4
my_class_attribute --> mock_4
my_instance_attribute --> mock_4
this_should_stay_the_same --> DO NOT MOCK ME
my_class_method --> mock_4
this_should_work_the_same --> DO NOT MOCK ME
my_class_static_method --> mock_4

```

**Happy coding**
