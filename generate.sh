#!/bin/bash

# 生成するモジュール名の配列
MODULES=("auth" "pricing" "billing" "awsmarketplace" "integration" "apilog" "communication" )

# sdkに含まれる生成したプログラムを削除
SDK_SRC_DIR="saasus_sdk_python/src"
SDK_TEST_DIR="test"

# 削除対象ディレクトリ
DELETE_DIRS=("generated")

for module in "${MODULES[@]}"
do
    if [ -d ${SDK_SRC_DIR}/${module} ]; then
        rm -rf ${SDK_SRC_DIR}/${module}
        echo "delete ${SDK_SRC_DIR}/${module} success"
    fi
    if [ -d ${SDK_TEST_DIR}/${module} ]; then
        rm -rf ${SDK_TEST_DIR}/${module}
        echo "delete ${SDK_TEST_DIR}/${module} success"
    fi
done

# pythondocを削除
rm -rf ./docs/*
echo "delete pythondoc success"

for dir in "${DELETE_DIRS[@]}"
do
    if [ -d ./${dir} ]; then
        rm -rf ./${dir}
    fi
done

#Pythonクラスを生成
for module in "${MODULES[@]}"
do
    if [ "${module}" = "integration" ]; then
        target="/local/${module}.yml"
    else
        target="/local/${module}api.yml"
    fi

    # don't use v7.3.0
    # https://github.com/OpenAPITools/openapi-generator/issues/17863
    docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v7.0.0 generate \
    -i ${target} \
    -g python \
    -o /local/saasus_sdk_python/generated/ \
    --additional-properties useOneOfDiscriminatorLookup=true \
    --package-name saasus_sdk_python.src.${module}
done

for module in "${MODULES[@]}"
do
    # プログラム
    cp -pr "saasus_sdk_python/generated/${SDK_SRC_DIR}/${module}" "${SDK_SRC_DIR}/${module}"
    # テストケース
    cp -pr "saasus_sdk_python/generated/${SDK_SRC_DIR}/${module}" "${SDK_TEST_DIR}/${module}"
    # pythondoc
    mkdir -p "docs/${module}" && cp -p saasus_sdk_python/generated/docs/* "docs/${module}/"
    echo "copy ${module} success"
done

# 生成したプログラムを削除
rm -rf ./saasus_sdk_python/generated
echo "delete generated success"