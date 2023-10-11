import uvicorn
from fastapi import FastAPI
from main import win_Model, win_quaility

# 2. Create the app object
app = FastAPI()
model = win_Model()


@app.post('/predict')
def predict_quality(alc: win_quaility):
    data = alc.dict()
    prediction, probablity = model.predict_quality(
        data['fixed_acidity'], data['volatile_acidity'], data['citric_acid'], 
        data['residual_sugar'], data['chlorides'], data['free_sulfur_dioxide'], data['total_sulfur_dioxide'],
        data['density'], data['pH'], data['sulphates'], data['alcohol']
        #fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol
    )
    return {
        'Оценка вина': str(prediction),
        'вероятность' : probablity

    }

#7.1,0.35,0.29,2.5,0.096,20.0,53.0,0.9962,3.42,0.65,11.0 
# 5. Run the API with uvicorn
#uvicorn fapi:app --reload
#Отображать в реальном времени
if __name__ == "__main__":
    uvicorn.run("fapi:app", host="127.0.0.1", port=5000, reload=True, access_log=False)


