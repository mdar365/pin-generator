### Setup Instructions
To run the application, you need Python v3.9.6. To download the required modules, run the following command (Make sure you are in the project's root directory):

`pip install -r requirements.txt`

Afterwards, you can manually test the library by running the main.py file

`python main.py`

This calls `generate_thousand_unique_pins()` which will print 1000 random PIN codes. The codebase for this library can be found under the pin_generator directory


### Automated Tests
There are three sets of tests. To run the tests, use the following commands:

`python pin_generator\tests\digit_generation_test.py` For testing single-digit generation logic

`python pin_generator\tests\multi_digit_generation_test.py` For testing generating numbers with multiple digits

`python pin_generator\tests\pin_generator_test.py` Testing PIN-generator functions
