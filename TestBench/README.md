<h1 style="color:#ffaa00; border-bottom: 2px dotted #ff00aa" >Generate Test scripts </h1>

before generating the test scripts we have to generate the which are tests exists in the ```IVM6311_Testing_scripts.xlsx``` test script 

<h3>Generate the Test Scripts configuration yaml file </h3>

* Run method ``` dump_test_names(self,testscripts_generate_config_file_path:Path) ``` from testCreate.py 

* Provide testscripts_generate_config_file_path yaml file path as input to store all the tests 
* If you run the following dump_test_names from testCreate.py  you can see test scripts config file under the test bench repository <br>
 ``` 
    if __name__ == '__main__': 
    testCreate = TestCreate(sheets = ['Digital','Reference','Boost']) 
    testCreate.dump_test_names('TestBench/testscript_generate_config.yaml') 
``` 
</br>

* Run testCreate script from terminal ``` python testCreate.py```