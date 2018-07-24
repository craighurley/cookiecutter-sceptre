#!/usr/bin/env bash

set -e

p=$(dirname "$0")

# sort requirements
find "$p" -type f -name "requirements.txt" -exec sh -c "sort {} > {}.clean ; rm {} ; rename -x {}.clean" \;

# format templates
find "$p"/templates -type f -name "*.yaml" -exec cfn-flip -cn {} {}.clean \;
rm "$p"/templates/*.yaml
rename -x "$p"/templates/*.clean

# confirm templates are valid yaml
yamllint -c "$p"/.yamllint "$p"/templates/
