#!/bin/sh

DH="south"
DATE="March 19th"
MEAL="Breakfast"

while [ "$#" -gt 0 ] 
do
    if [ "$1" == "-h" ]; then
        shift
        DH="$1"
    fi
    if [ "$1" == "-d" ]; then
        shift
        DATE="$1"
    fi
    if [ "$1" == "-m" ]; then
        shift
        MEAL="$1"
    fi
    shift
done

# will need to use more then grep to extract the information but hopefully will figure out what the right commands are                                                          # once I figure out how to access the menu items in the container 
curl -s http://dining.nd.edu/locations-menus/"$DH"-dining-hall/ | grep -E '$DATE' | grep -E '$MEAL' | grep -E 'menu-item-name' | grep -Eo '>.*<' | tee menuitems.txt  


