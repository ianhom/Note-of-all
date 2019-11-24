#!/bin/bash
sudo apt-get install pv
eche "Hello World!" | pv -qL 10
