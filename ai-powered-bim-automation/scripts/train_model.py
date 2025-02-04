from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def train_clash_model(data_path):
    """Train a simple AI model to predict clashes."""
    data = pd.read_csv(data_path)
    X = data.drop("clash", axis=1)
    y = data["clash"]
    
    model = DecisionTreeClassifier()
    model.fit(X, y)
    
    return model

def predict_clashes(model, new_data):
    """Predict clashes using the trained model."""
    return model.predict(new_data)