from clipper_admin.deployers import python as python_deployer
from clipper_admin import ClipperConnection, DockerContainerManager
from clipper_admin.exceptions import ClipperException
from docker.errors import APIError
import json
import requests

# Set up connection
clipper_conn = ClipperConnection(
    DockerContainerManager()
)

try:
    clipper_conn.start_clipper()
except (APIError, ClipperException):
    clipper_conn.connect()

# Deploy Sum function
clipper_conn.register_application(
    name="Sum", input_type="doubles", default_output="-1.0", slo_micros=100000)


# Define model func
def feature_sum(xs):
    return [str(sum(x)) for x in xs]


# Deploy python model
python_deployer.deploy_python_closure(
    clipper_conn,
    name="sum-model",
    version=1,
    input_type="doubles",
    func=feature_sum
)

data = json.dumps({
    "app_name": "Sum",
    "model_names": [
        "sum-model"
    ]
})
r = requests.post('http://localhost:1338/admin/add_model_links', data=data)
print(r.status_code, r.text)

# Deploy average function
clipper_conn.register_application(
    name="Average", input_type="doubles", default_output="-1.0", slo_micros=100000)


# Define model func
def feature_average(xs):
    return [(str(sum(x)/len(x)) if len(x) > 0 else "Cannot average 0 elements") for x in xs]


# Deploy python model
python_deployer.deploy_python_closure(
    clipper_conn,
    name="avg-model",
    version=1,
    input_type="doubles",
    func=feature_average
)

data = json.dumps({
    "app_name": "Average",
    "model_names": [
        "avg-model"
    ]
})
r = requests.post('http://localhost:1338/admin/add_model_links', data=data)
print(r.status_code, r.text)
