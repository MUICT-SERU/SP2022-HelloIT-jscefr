#!/bin/sh

# $1 = project name
# $2 = scoring type MAX | ALL

# Run JSCEFR
pwd
cd ../jscefr_tool
python jscefr.py directory dataset/$1

cd ../experiment

# Run data extraction
python report_generators/generate_dataset.py $1 $2

# Run data analysis
python statistical-test/extract_summary_new.py $1 $2
python statistical-test/correlation_analysis.py $1 $2
python statistical-test/statistical_dif_test.py $1 $2

# Run data visualization
python statistical-test/new_visualization_other.py $1 $2
python statistical-test/new_visualization_test.py $1 $2