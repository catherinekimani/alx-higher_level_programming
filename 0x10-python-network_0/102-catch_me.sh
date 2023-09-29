#!/bin/bash
# script that makes a request that causes the server to respond given message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
