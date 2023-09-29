#!/bin/bash
# script that takes in a URL, sends a request displays size of the body
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
