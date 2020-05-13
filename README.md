# tf_cnn_model_load_testing
### create virtual environment using 
virtualenv <env_name>
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
