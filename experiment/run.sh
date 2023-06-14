#!/bin/sh

# $1 = project name
# $2 = scoring type

# Run JSCEFR
python jscefr.py directory input_dataset/$1

# Run data extraction
python report_generators/generate_dataset.py $1 $2

# Run data analysis
python statistical-test/extract_summary_new.py $1 $2
python statistical-test/correlation_analysis.py $1 $2
python statistical-test/statistical_dif_test.py $1 $2

# Run data visualization
python statistical-test/new_visualization_other.py $1 $2
python statistical-test/new_visualization_test.py $1 $2