#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sL -X "GET" -H "X-HolbertonSchool-User-Id:98" "$1" 
