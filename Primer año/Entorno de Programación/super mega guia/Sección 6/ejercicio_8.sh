#! /bin/bash

tr '[:space:]' '\n' < archivo.txt | tr -d ',.' | sort | uniq -c | sort -nr | head -n 5
