from clipper_admin import ClipperConnection, DockerContainerManager 
from docker.errors import APIError

clipper_conn = ClipperConnection(DockerContainerManager()) 
try:
    clipper_conn.start_clipper()
except APIError:
    clipper_conn.connect()
