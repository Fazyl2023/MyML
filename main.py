import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


class lap_Species(BaseModel):
    Model_Name: str 
    Category: str 
    Operating_System_Version: str 



# 3. Class for training the model and making predictions
class lap_Model:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = pd.read_csv('laptops_train.csv')
        
        self.model_fname_ = 'save.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop('Manufacturer', axis=1)
        y = self.df['Manufacturer']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_species(self, Model_Name, Category, Operating_System_Version):
        data_in = [[Model_Name, Category, Operating_System_Version, Operating_System_Version]]
        prediction = self.model.predict(data_in)
        
        return prediction['this']