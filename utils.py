import pandas as pd
import numpy as np
import pickle 
import json
import config

class CarPrice():
    def __init__(self):
        self.__load_data()

    def __load_data(self):
        with open(config.MODEL_FILE_NAME, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.COLUMN_DATA_JSON, 'r') as f:
            self.column_data = json.load(f)
        
        self.column_names = self.model.feature_names_in_
        self.features_count = self.model.n_features_in_

    def predicted_results(self, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner):
        self.__load_data()
        Fuel_Type = self.column_data['Fuel_Type'][Fuel_Type]
        Seller_Type = self.column_data['Seller_Type'][Seller_Type]
        Transmission = self.column_data['Transmission'][Transmission]

        test_array = np.zeros((1, self.features_count)) 
        test_array[0, 0] = Present_Price
        test_array[0, 1] = Kms_Driven
        test_array[0, 2] = Fuel_Type
        test_array[0, 3] = Seller_Type
        test_array[0, 4] = Transmission
        test_array[0, 5] = Owner
        
        predicted_results = self.model.predict(test_array)[0]
    
        return predicted_results

def load_dataset():
    df = pd.read_csv(config.CSV_FILE_NAME)
    # print(df)
    return df