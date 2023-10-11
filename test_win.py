from fastapi.testclient import TestClient
from fapi import app


client = TestClient(app)
##,,,,,,,
def test_read_predict_3():
        response = client.post("/predict/",json={"fixed_acidity": 7.4,
                                                 "volatile_acidity": 1.185,
                                                 "citric_acid": 0,
                                                 "residual_sugar": 4.25,
                                                 "chlorides": 0.09699999,
                                                 "free_sulfur_dioxide": 5,
                                                 "total_sulfur_dioxide": 14,
                                                 "density": 0.9966, 
                                                 "pH": 3.63, 
                                                 "sulphates": 0.54, 
                                                 "alcohol": 10.7})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "3"
#,,,,,,
def test_read_predict_4():
        response = client.post("/predict/",json={"fixed_acidity": 6.4,
                                                 "volatile_acidity": 0.53,
                                                 "citric_acid": 0.09,
                                                 "residual_sugar": 3.9,
                                                 "chlorides": 0.12300000000000001,
                                                 "free_sulfur_dioxide": 14.0,
                                                 "total_sulfur_dioxide": 31.0,
                                                 "density": 0.996, 
                                                 "pH": 3.5, 
                                                 "sulphates": 0.67, 
                                                 "alcohol": 11})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "4"

#,,,,,,
def test_read_predict_5():
        response = client.post("/predict/",json={
                                                
                                                 "fixed_acidity": 8.2,
                                                 "volatile_acidity": 0.28,
                                                 "citric_acid": 0.6,
                                                 "residual_sugar": 3.0,
                                                 "chlorides": 0.10400000000000001,
                                                 "free_sulfur_dioxide": 10,
                                                 "total_sulfur_dioxide": 22,
                                                 "density": 0.99828,
                                                 "pH": 3.39, 
                                                 "sulphates": 0.68, 
                                                 "alcohol": 10.6
         })
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "5"

#,,,,,,,,,
def test_read_predict_6():
        response = client.post("/predict/",json={
 "fixed_acidity": 6.9,
  "volatile_acidity": 0.74,
  "citric_acid": 0.03,
  "residual_sugar": 2.3,
  "chlorides": 0.054000000000000006,
  "free_sulfur_dioxide": 7,
  "total_sulfur_dioxide": 16.0,
  "density": 0.99508,
  "pH": 3.45,
  "sulphates": 0.63,
  "alcohol": 11.5
})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "6"


def test_read_predict_7():
        response = client.post("/predict/",json={
  "fixed_acidity": 12.8,
  "volatile_acidity": 0.3,
  "citric_acid": 0.74,
  "residual_sugar": 2.6,
  "chlorides": 0.095,
  "free_sulfur_dioxide": 9,
  "total_sulfur_dioxide": 28,
  "density": 0.9994,
  "pH": 3.2,
  "sulphates": 0.77,
  "alcohol": 10.8
})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "7"

def test_read_predict_8():
        response = client.post("/predict/",json={
  "fixed_acidity": 12.6,
  "volatile_acidity": 0.31,
  "citric_acid": 0.72,
  "residual_sugar": 2.2,
  "chlorides": 0.0721,
  "free_sulfur_dioxide": 6,
  "total_sulfur_dioxide": 29,
  "density": 0.9987,
  "pH": 2.88,
  "sulphates": 0.82,
  "alcohol": 9.8
})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "8"




#7.5,0.38,0.48,2.6,0.073,22.0,84.0,0.9972,3.32,0.7,9.6,4

