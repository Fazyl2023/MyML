from fastapi.testclient import TestClient
from fapi import app


client = TestClient(app)

def test_read_predict_5():
        response = client.post("/predict/",json={"fixed_acidity": 0,
                                                 "volatile_acidity": 0,
                                                 "citric_acid": 0,
                                                 "residual_sugar": 0,
                                                 "chlorides": 0,
                                                 "free_sulfur_dioxide": 0,
                                                 "total_sulfur_dioxide": 0,
                                                 "density": 0, 
                                                 "pH": 0, 
                                                 "sulphates": 0, 
                                                 "alcohol": 0})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data['Оценка вина'] == "5"


def test_read_predict_6():
        response = client.post("/predict/",json={
 "fixed_acidity": 7,
  "volatile_acidity": 1,
  "citric_acid": 1,
  "residual_sugar": 1,
  "chlorides": 0.09,
  "free_sulfur_dioxide": 35,
  "total_sulfur_dioxide": 52,
  "density": 0.99,
  "pH": 1,
  "sulphates": 1,
  "alcohol": 5
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

##

