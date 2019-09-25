To build the clipper image run:

```docker build -t adalitix/clipper-dev .```

To launch it run:

```docker run --rm -it --link dind:docker adalitix/clipper-dev sh ```

To start clipper and test it run:

```python3 start_clipper.py ```

and

```python3 test_clipper_connection.py```
