#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -I $1 2>/dev/null | grep Content-Length | sed 's/[^0-9]*//g'
