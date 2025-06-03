#! /bin/bash

grep -Eo '[[:alnum:].]*@[[:alpha:]]*.com(.ar)?' ./emails.txt
