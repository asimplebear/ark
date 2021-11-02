#!/bin/bash

#arg is string. Echos first 16 chars
#of the sha256 hash of input string
echo $1 | sha256sum | cut -c1-16
