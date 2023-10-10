import uvicorn
from fastapi import FastAPI
from main import lap_Model, lap_Species

# 2. Create the app object
app = FastAPI()
model = lap_Model()


@app.post('/predict')
def predict_species(iris: lap_Species):
    data = iris.dict()
    prediction = model.predict_species(
        data['Model_Name'], data['Category'], data['Operating_System_Version']
    )
    return {
        'company': prediction
    }


# 5. Run the API with uvicorn
#Отображать в реальном времени
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 
