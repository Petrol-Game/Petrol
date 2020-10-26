#!/bin/bash

#this cannot be used to build, as it currently does not fully work, just manully zip the files and folders needed

echo Output file name:

read outname

zip $outname ./SRC/petrol.py ./SRC/petrolasset.py ./SRC/__main__.py ./SRC/ASSETS

echo Done!