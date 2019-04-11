#!/bin/bash
# takes in a URL, sends a POST request to that URL, and displays the size of the body of the response
curl -X "POST" "$1" -sd "subject=I will always be here for PLD&email=hr@holbertonschool.com"
