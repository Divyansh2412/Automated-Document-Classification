import KNN as KNN
import DatasetManager as DM
import DocumentPreprocessing as DC
from sklearn.model_selection import train_test_split

datapath = r"C:\Users\dmiya\Desktop\major\model\Automated-Document-Classification\dataset\BBC News Train.csv"
testpath = r"C:\Users\dmiya\Desktop\major\model\Automated-Document-Classification\test documents\test10.txt"
X, Y = DM.preprocess(datapath)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=.2)

# Print shapes for debugging
print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)
print("X_test shape:", X_test.shape)
print("Y_test shape:", Y_test.shape)

# KNN Model
KNN.KNN(X_train, X_test, Y_train, Y_test)

print("--------------Document Prediction ----------------")
document = DC.PredictDocument(testpath)

# Ensure the document is reshaped properly if needed
if len(document.shape) == 1:
    document = document.reshape(1, -1)
print(KNN.model.predict(document))

