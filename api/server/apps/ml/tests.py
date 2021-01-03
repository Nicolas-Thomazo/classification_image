from django.test import TestCase
# add at the beginning of the file:
import inspect
from apps.ml.registry import MLRegistry

from apps.ml.income_classifier.random_forest import RandomForestClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "col1": [1,2],
            "col2": [1,2],
            "col3": [1,2],
            "col4":[1,2]}
            
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        #response = {"Classe": "yes", "status": "OK"}
        print(response)
        print("coccc")
        self.assertEqual('OK', response['status'])
        #self.assertEqual('', response['label'])
    
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Piotr"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

    