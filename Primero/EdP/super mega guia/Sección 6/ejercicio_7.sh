#! /bin/bash

cut -d - -f 1 ./access.log | sort | uniq
