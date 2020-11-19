import argparse
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error
import json
import io

def test_model(model,x_test, y_test):
    x_test_data = np.load(x_test)
    y_test_data = np.load(y_test)

    model = joblib.load(model)
    y_pred = model.predict(x_test_data)

    err = mean_squared_error(y_test_data, y_pred)
    print(str(err))
    
    with open('output.txt', 'a') as f:
        f.write(str(err))
        
    # write out metrics
    metrics = {
        'metrics': [{
          'name': 'accuracy-score',
          'numberValue':  err,
          'format': "PERCENTAGE",
        }]
    }

    with open('/mlpipeline-metrics.json', 'w') as fo:
        json.dump(metrics, fo)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    args = parser.parse_args()
    test_model(args.model, args.x_test, args.y_test)
    