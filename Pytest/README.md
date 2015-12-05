# PyTest

##Installation

Installation options:

        pip install -U pytest # or
        easy_install -U pytest # or
        pip install -r requirements.txt # inside the file: pytest>=2.8.3
        
Checking version of your installation:

        $ py.test --version
        This is pytest version 2.8.3, imported from $PYTHON_PREFIX\lib\site-packages\pytest.pyc 
        # or
        This is pytest version 2.8.3, imported from $PYTHON_PREFIX/lib/site-packages/pytest.py

Simple test function

        py.test simple_test_function.py

Running multiple tests

        py.test   # will run all files and tests with names starting with test_
                  # or ending with _test, like test_first.py or second_test.py

