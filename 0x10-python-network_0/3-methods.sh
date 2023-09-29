#!/bin/bash
# script that takes in a URL & displays all HTTP methods the server will accept
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
