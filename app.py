from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('A1_Car.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def result():
    transmission = request.form['Transmission']
    fuel = request.form['Fuel']
    driven = float(request.form['driven'])
    year = float(request.form['year'])
    engine = float(request.form['Engine'])

    #Process the input as per your requirements
    fuel = 1 if fuel.lower() == 'petrol' else 0
    transmission = 1 if transmission.lower() == 'automatic' else 0

    # Take the log of driven
    driven = np.log(driven)

    # Prepare the input for prediction
    input_data = np.array([[fuel,transmission, driven, year, engine]])

    # Make prediction using the loaded model
    prediction = model.predict(input_data)


    return render_template('index.html',data=prediction)

if __name__ =='__main__':
    app.run(debug=True)