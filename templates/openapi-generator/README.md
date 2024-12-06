# Custom OpenAPI Generator Templates

## Overview
This directory contains custom templates for the OpenAPI Generator. These templates are based on the standard Python templates for version `v7.0.0`, with minor adjustments to support specific project requirements.

## Customizations
### File: `model_oneof.mustache`
- **Modification**: 
  - A minor change was made to add type hints for `discriminator_value_class_map` to resolve issues when using `bump-pydantic` with Pydantic v2.
  - This ensures the generated code complies with type checking and avoids runtime errors.

- **Before:**
  ```python
  discriminator_value_class_map = {
  ```

- **After:**
  ```python
  discriminator_value_class_map: Dict[str, str] = {
  ```

### Purpose
- This change ensures compatibility with Pydantic v2, which expects explicit type annotations for better type checking and runtime behavior.

## Impact
- This customization affects only files generated with the `model_oneof.mustache` template.
- Other templates remain unchanged and follow the default behavior of OpenAPI Generator v7.0.0.

## Usage
When generating SDK code, specify the custom templates using the `--template-dir` option in your `generate.sh` script. For example:
```bash
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v7.0.0 generate \
  -i ${target} \
  -g python \
  --template-dir /local/templates/openapi-generator/python-v7.0.0/ \
  -o /local/saasus_sdk_python/generated/ \
  --additional-properties useOneOfDiscriminatorLookup=true \
  --package-name saasus_sdk_python.src.${module}
```
