#!/bin/bash

docker build -t paolodenti/pytest -t paolodenti/pytest:1.0.0 .
docker push --all-tags paolodenti/pytest
