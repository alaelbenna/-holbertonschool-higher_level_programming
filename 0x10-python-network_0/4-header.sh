#!/bin/bash
#takes URL, sends GET request display body
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id: 98'
