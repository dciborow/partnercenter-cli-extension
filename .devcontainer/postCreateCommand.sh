#!/bin/bash

python -m pip install setuptools wheel twine

cd partnercenter
python setup.py sdist bdist_wheel
az extension add \
    --yes \
    --upgrade \
    --source dist/partnercenter-*-py3-none-any.whl
