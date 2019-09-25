#!/bin/sh

# wait until docker daemon is working
until docker ps > /dev/null 2>&1; do
  >&2 echo "Waiting for docker daemon ..."
  sleep 1
done

>&2 echo "Docker is up - setting up clipper"

python3 start_clipper.py
python3 deploy_example_function.py