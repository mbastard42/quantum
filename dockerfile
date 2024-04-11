FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    git \
    python3-pip

RUN pip install --upgrade pip \
    qiskit \
    qiskit-ibm-runtime

ENTRYPOINT ["bash"]
