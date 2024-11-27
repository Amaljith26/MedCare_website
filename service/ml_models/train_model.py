import os
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Get the dataset's path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset_path = os.path.join(BASE_DIR, 'datasets', 'heart_data.csv')

# Check if dataset exists
if os.path.exists(dataset_path):
    heart_data = pd.read_csv(dataset_path)
else:
    print(f"Dataset not found at {dataset_path}")
    exit()

# Check the first 10 rows and data info
print(heart_data.head(10))
print(heart_data.info())

# Handle missing values (if any)
if heart_data.isnull().sum().any():
    print("Missing values found. Filling missing values.")
    heart_data.fillna(method='ffill', inplace=True)

# Check target value distribution
print(heart_data["target"].value_counts())

# Split the dataset
X = heart_data.drop(columns="target", axis=1)
y = heart_data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=2, stratify=y)

print(f"Original shape: {X.shape}, Training shape: {X_train.shape}, Test shape: {X_test.shape}")

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Define paths for saving model and scaler
model_dir = os.path.join(BASE_DIR, 'new_data')  # Folder for model files
scaler_dir = os.path.join(BASE_DIR, 'new_data')  # Folder for scaler files

# Create directories if they don't exist
os.makedirs(model_dir, exist_ok=True)
os.makedirs(scaler_dir, exist_ok=True)

# Define full paths for saving the model and scaler
model_path = os.path.join(model_dir, 'train_model.pkl')  # Full path for model file
scaler_path = os.path.join(scaler_dir, 'scaler.pkl')  # Full path for scaler file

# Save the model
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

# Save the scaler
with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print(f"Model saved at {model_path}")
print(f"Scaler saved at {scaler_path}")
