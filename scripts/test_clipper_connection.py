import numpy as np
import requests
import json


data = json.dumps({
    "batch_size": 10,
    "container_name": "sum-model:1:0",
    "input_type": "doubles",
    "model_name": "sum-model",
    "model_version": "1",
    "labels": [
        "TeamDevOps"
    ],
    "model_data_path": "/tmp/clipper/sum-model-data/"
})
r = requests.post('http://localhost:1338/admin/add_model', data=data)
print('Link')
print(r.status_code, r.text)
print()


data = json.dumps({
    "app_name": "hello-world",
    "model_names": [
        "sum-model"
    ]
})
r = requests.post('http://localhost:1338/admin/add_model_links', data=data)
print('Link')
print(r.status_code, r.text)
print()


data = json.dumps({"verbose": True})

r = requests.post(
    'http://localhost:1338/admin/get_all_applications', data=data)
print('Applications')
print(r.status_code, r.text)
print()

r = requests.post('http://localhost:1338/admin/get_all_containers', data=data)
print('Containers')
print(r.status_code, r.text)
print()


r = requests.post('http://localhost:1338/admin/get_all_models', data=data)
print('Models')
print(r.status_code, r.text)
print()


data = json.dumps({"input": list(np.random.random(10))})
r = requests.post("http://localhost:1337/hello-world/predict", data=data)
print("Example call")
print(r.status_code, r.text)
print()
