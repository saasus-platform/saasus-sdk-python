#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <package_name>"
    echo "Example: $0 authapi"
    exit 1
fi

packageName=$1

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/${packageName}.yml \
    -g python \
    -o /local \
    --package-name saasus_sdk_python
