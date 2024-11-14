from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import joblib

def predict_model(X_train, X_test, Y_train, Y_test):
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf'],
        'gamma': ['scale', 'auto']
    }

    grid_search = GridSearchCV(SVC(probability=True), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, Y_train)
    
    print(f'Best parameters: {grid_search.best_params_}')
    best_svm_model = grid_search.best_estimator_
    
    y_pred = best_svm_model.predict(X_test)
    print(classification_report(Y_test, y_pred))
    
    joblib.dump(best_svm_model, './models/svm_model.pkl')
