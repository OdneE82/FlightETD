# Demonstration of model in Flask application
I created a quick flask application that gathers the Avinor flydata, and also applies the simpler machine learning model.

## Installation
### Clone the Repository
First, clone the FlightETD repository from Github to your local machine:

```git
git clone https://github.com/OdneE82/FlightETD.git
cd FlightETD
```
### Set up a Virtual Enviroment
It's recommended to run Python projects in a virtual enviroment to manage dependencies efficiently. Create and activate a virtual enviroment in the repository's root directory:
```git
python3 -m venv venv
source venv/bin/activate
```
On Windows, the activation command is slightly different:
```git
venv\Scripts\activate.bat
```

### Install Flask
Install dependencies
```git
pip install -r requirements.txt
```

### Run the models Notebook
Before starting the Flask application, run the notebook that saves the model, this is because the model size is too large for github. Ensure that you are in the flask applications folder /flaskr
```git
jupyter notebook model.ipynb
```

## Starting the Flask application
Navigate to the `/flaskr`directory. then start the Flask application by running:
```git
flask run
```

### Accessing the application
Once the Flask server is running, you can access the application by navigating to the following URL in your browser
```git
http://127.0.0.1:5000/
```
