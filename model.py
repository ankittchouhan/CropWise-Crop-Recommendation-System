import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# 1. Load the dataset
data = pd.read_csv('crop_data.csv')  # Path to the dataset

# 2. Preprocessing - Features and Target Variable
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]  # Features
y = data['label']  # Target variable (label)

# 3. Split the dataset into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Model evaluation on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 6. Save the trained model to a file for future use
with open('crop_recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model has been saved as 'crop_recommendation_model.pkl'")
