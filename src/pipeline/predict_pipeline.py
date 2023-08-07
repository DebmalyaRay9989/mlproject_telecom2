import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            #model_path = os.path.join("artifacts", "model.pkl")
            #preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path: str=os.path.join('artifacts',"model.pkl")
            preprocessor_path: str=os.path.join('artifacts',"preprocessor.pkl")
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            print(preds)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 SIM_COMPANY: str,
                 VALIDITY: str,
                 DATA_PER_DAY: str,
                 ADDITIONAL_DATA: str,
                 SMS_PER_DAY: str,
                 ADDITIONAL_SMS: str,
                 DISNEY_HOTSTAR: str,
                 COST_PER_DAY: str):

        self.SIM_COMPANY = SIM_COMPANY

        self.VALIDITY = VALIDITY

        self.DATA_PER_DAY = DATA_PER_DAY

        self.ADDITIONAL_DATA = ADDITIONAL_DATA

        self.SMS_PER_DAY = SMS_PER_DAY

        self.ADDITIONAL_SMS = ADDITIONAL_SMS

        self.DISNEY_HOTSTAR = DISNEY_HOTSTAR

        self.COST_PER_DAY = COST_PER_DAY

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "SIM_COMPANY": [self.SIM_COMPANY],
                "VALIDITY": [self.VALIDITY],
                "DATA_PER_DAY": [self.DATA_PER_DAY],
                "ADDITIONAL_DATA": [self.ADDITIONAL_DATA],
                "SMS_PER_DAY": [self.SMS_PER_DAY],
                "ADDITIONAL_SMS": [self.ADDITIONAL_SMS],
                "DISNEY_HOTSTAR": [self.DISNEY_HOTSTAR],
                "COST_PER_DAY": [self.COST_PER_DAY]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


