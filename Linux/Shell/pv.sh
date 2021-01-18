#!/bin/bash
sudo apt-get install pv
echo "Hello World!" | pv -qL 10
