from flask import Flask, render_template, request, jsonify
from utils import CarPrice,load_dataset
from flask_cors import CORS

df=load_dataset()
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuel_options')
def fuel_options():
    return jsonify(list(df['Fuel_Type'].unique()))

@app.route('/seller_options')
def seller_options():
    return jsonify(list(df['Seller_Type'].unique()))

@app.route('/transmission_options')
def transmission_options():
    return jsonify(list(df['Transmission'].unique()))

@app.route('/prediction', methods=['POST'])
def prediction():
    data = request.form.to_dict() # For JSON data
    print(data)

    Present_Price = data['Present_Price']
    Kms_Driven = data['Kms_Driven']
    Fuel_Type = data['Fuel_Type']
    Seller_Type = data['Seller_Type']
    Transmission = data['Transmission']
    Owner = data['Owner']

    carprice = CarPrice()
    pred_price = carprice.predicted_results(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
    return jsonify(pred_price)

if __name__ == "__main__":
    app.run( port='5050', debug=True)