from models import Model

def predict(data):
    model = Model()
    return model.model.predict(data)
