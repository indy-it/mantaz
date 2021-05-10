#!/bin/bash
mkdir -p Editor_results/all/csv1
mkdir -p Editor_results/all/csv2
cd Editor_results/
ls > ../fra1.txt
ditto * all/
cd all
mv 1pop* csv1/
mv 2pop* csv2/
cp csv1/*  /Users/dani/Documents/MATLAB/Csv-paper/csv1
cp csv2/* /Users/dani/Documents/MATLAB/Csv-paper/csv2
