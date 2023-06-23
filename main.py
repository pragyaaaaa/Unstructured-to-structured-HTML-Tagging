# Import the necessary functions from the feature_extraction module
from feature_extraction import heading_extraction 
from feature_extraction import figure_heading_extraction 
from feature_extraction import table_heading_extraction 
from feature_extraction import tagging 

# Call the functions in the desired sequence
heading_extraction()
figure_heading_extraction()
table_heading_extraction()
tagging()
