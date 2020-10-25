# EPAi session12 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session12 objectives
This assignment, helps to code the concepts that are learnt in the session 12 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

 - Packages
 - Why Packages
 - Namespace Packages
 
---

The test cases can be executed by executing _pytest_, from python shell

## Assignment

 - Build a calculator package that has separate module for:
sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
 - The modules shall include their derivatives as well
 - If we do import calculator, we should be able to access all the above function (except deviratives)
 - For derivates we must do: from package import derivatives. 
 - Outputs are returned as well as printed using only f-string
 - Write simple test cases to check the outputs of each operator and their derivative 

---

### Unit Tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_cos()**

    Test the method cos in the calculator package
     : return :  None

**test_exp()**

    Test the method exp in the calculator package
     : return :  None

**test_log()**

    Test the method log in the calculator package
     : return :  None

**test_relu()**

    Test the method relu in the calculator package
     : return :  None

**test_sigmoid()**

    Test the method sigmoid in the calculator package
     : return :  None

**test_sin()**

    Test the method sin in the calculator package
     : return :  None

**test_softmax()**

    Test the method softmax in the calculator package
     : return :  None

**test_tan()**

    Test the method tan in the calculator package
     : return :  None

**test_tanh()**

    Test the method tanh in the calculator package
     : return :  None


---

#### 