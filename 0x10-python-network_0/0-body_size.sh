#!/bin/bash
#Script takes a URL, sends a request to URL, displays size of body of response.
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
