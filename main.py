import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib
from sklearn import datasets


class win_quaility(BaseModel):
    fixed_acidity: float 
    volatile_acidity: float 
    citric_acid: float 
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float 
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float 
    alcohol: float
    #fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol


# 3. Class for training the model and making predictions
class win_Model:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = pd.read_csv('winRed.csv')
        
        self.model_fname_ = 'model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop('quality', axis=1)
        y = self.df['quality']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_quality(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,total_sulfur_dioxide, density, pH, sulphates, alcohol):
        data_in = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,total_sulfur_dioxide, density, pH, sulphates, alcohol]]
        #prediction = self.model.predict(data_in)
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability