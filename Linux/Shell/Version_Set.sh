#!/bin/bash

rm -f version

eche -e "THE HARDWARE VERSION:\n$1" > version

cat version
