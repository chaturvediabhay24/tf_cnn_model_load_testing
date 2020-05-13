# tf_cnn_model_load_testing
### create virtual environment using :
'''shell
virtualenv <env_name>
'''
### change the directory
cd <env_name>
### clone this repository
git clone https://github.com/chaturvediabhay24/tf_cnn_model_load_testing.git
### change the directory
cd tf_cnn_model_load_testing
### install dependencies
pip install -r requirements.txt
### run these two command parallely in two different shells
##### for running api:
python app.py
##### for running locust:
locust
#### For viewing api open http://127.0.0.1:5000
#### For viewing locust ui open http://localhost:8089
##### Enter the number of users, hatch rate and host(http://127.0.0.1:5000) to start the test.
