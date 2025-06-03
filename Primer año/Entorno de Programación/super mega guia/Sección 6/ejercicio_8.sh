#! /bin/bash

tr '[:space:]' '\n' < archivo.txt | tr -d ',.' | grep -E '^.' | sort | uniq -c | sort -nr | head -n 5
