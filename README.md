## Namespace python exercise
### Why
- I realised that most issues encountered by developers while trying to write python unit tests are due to a misunderstanding about how the library `unittest.mock` works and especially the `patch`function. This exercise aims to implement the `patch` logic without using any libraries.
- You will need to patch python classes and modules

### TLDR: Exercise instructions:
- Clone the repo
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
- You should not patch the `main.run` method itself (ie `main.run = lambda: print(expected output)`)
- You should not use any external or standard python library

**Context:**
- A simple python `package` with one submodule `module1.py`  with different kind of objects:
    - one constant
    - one function
    - one class with
       - two class attribute
       - one instance attribute
       - two method
       - one static method

- A `main.py` that:
   - import different things:
      - import the package
      - import the submodule
      - import the python objects from the `package/__init__.py` files
      - import the python objects from the `module1.py` files
   - a `run` function that prints the results of all the methods and object:

- I wrote a `test_main.py` where I execute this function:

I you execute the main.run() with `python3 test_main.py`  you should get the following output:

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
