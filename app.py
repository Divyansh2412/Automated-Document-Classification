import os
from flask import Flask, request, render_template
import KNN as KNN
import DatasetManager as DM
import DocumentPreprocessing as DC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load and preprocess your dataset
datapath = r"C:\Users\dmiya\Desktop\major\model\Automated-Document-Classification\dataset\BBC News Train.csv"
X, Y = DM.preprocess(datapath)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=.2)

# Train your KNN model
knn_model = KNN.KNN(X_train, X_test, Y_train, Y_test)

# Calculate the accuracy of the model
Y_pred = KNN.model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        # Ensure the directory exists
        upload_dir = r"C:\Users\dmiya\Desktop\major\model\Automated-Document-Classification\test documents"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Construct the full file path
        file_path = os.path.join(upload_dir, file.filename)
        
        # Save the uploaded file
        file.save(file_path)
        
        try:
            # Process the uploaded file
            document = DC.PredictDocument(file_path)
            if len(document.shape) == 1:
                document = document.reshape(1, -1)
            
            # Get prediction using your KNN model
            prediction = KNN.model.predict(document)[0]
            print(f"Prediction: {prediction}, Accuracy: {accuracy}")

            # Render result page with prediction and accuracy
            return render_template('result.html', prediction=prediction, accuracy=accuracy, filename=file.filename)
        except Exception as e:
            print(f"Error processing file: {e}")
            return render_template('error.html', message="Error processing the file.")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
