#!/bin/bash
# script that makes a request that causes the server to respond given message
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
