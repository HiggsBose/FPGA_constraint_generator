### FPGA Pin Constraint Generator

This program automatically generates pin constraint used in Vivado. Pin definitions are extracted from a excel sheet or a .csv file, and the output constraints are in the format of plain text in the terminal.
The excel sheet or .csv file should countain the signal name, and the corresponding FPGA pin name, stored in a column-wise manner. This program also substitutes the '<>' in signal names with '[]' to support a bus wire. 
