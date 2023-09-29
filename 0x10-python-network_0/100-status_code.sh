#!/bin/bash
# script that sends a request to a URL passed as an argu & displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
