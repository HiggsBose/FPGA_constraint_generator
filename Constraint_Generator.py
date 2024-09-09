import csv
import pandas as pd


def excel_generator(address, sheet_name):
    """
    print the generated fpga pin assignment constraint using the excel file

    :param address: the file address
    :return: None
    """
    df = pd.read_excel(address, sheet_name=sheet_name)

    signal_name = "PIN Name"    # the name of the column of signal names in FPGA
    pin_type_name = "Type"      # Pin type definition, IN or OUT
    fpga_pin_name = "FPGA PIN"  # the name of the column of FPGA PIN names

    assert len(df[signal_name]) == len(df[fpga_pin_name])

    for index in range(len(df[signal_name])):
        if df[pin_type_name][index] != "IN" and df[pin_type_name][index] != "OUT":
            continue

        df[signal_name][index] = df[signal_name][index].replace("<", "[")
        df[signal_name][index] = df[signal_name][index].replace(">", "]")
        if "[" and "]" in df[signal_name][index]:
            df[signal_name][index] = "{" + df[signal_name][index] + "}"

        print("set_property IOSTANDARD LVCMOS33 [get_ports " + df[signal_name][index] + "]")
        print("set_property PACKAGE_PIN " + df[fpga_pin_name][index] + " [get_ports " + df[signal_name][index] + "]")


def csv_generator(file_name):
    """
    print the generated fpga pin assignment constraint using the csv file

    :param file_name: the address of the csv file with specific format
    :return: nothing

    """
    with open(file_name) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[-1] == '':
                continue
            # print(line)
            if "<" and ">" in line[0]:
                line[0] = line[0].replace("<", "[")
                line[0] = line[0].replace(">", "]")

            if "[" and "]" in line[0]:
                line[0] = "{" + line[0] + "}"

            print("set_property IOSTANDARD LVCMOS33 [get_ports " + line[0] + "]")
            print("set_property PACKAGE_PIN "+ line[-1] + " [get_ports " + line[0] + "]")

        file.close()


file_address = "file_address" # Please enter the address of the .xlsx or .csv file here
sheet_name = "sheet_name" # enter the sheet name
excel_generator(file_address, sheet_name)
