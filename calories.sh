#!/bin/sh

ITEM="English Muffins"
DH="South"
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

# will need to use more then grep to extract the information
curl -s https://nutrition.nd.edu/1# | grep -E '> "$DH" Daily Menus<' | grep -E '$DATE' | grep -E '$MEAL' | grep -E 'LabelHeader">"$ITEM"<' | grep -E '>[0-9]+<'  
