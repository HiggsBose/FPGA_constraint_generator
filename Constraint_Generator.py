import csv
import pandas as pd


def excel_generator(address, sheet_name):
    """
    print the generated fpga pin assignment constraint using the excel file

    :param address: the file address
    :return: None
    """
    df = pd.read_excel(address, sheet_name=sheet_name)

    signal_name = "Pin Name"
    pin_type_name = "类型"
    fpga_pin_name = "FPGA引脚"

    assert len(df[signal_name]) == len(df[fpga_pin_name])

    for index in range(len(df[signal_name])):
        if df[pin_type_name][index] != "S_4_IN" and df[pin_type_name][index] != "S_4_OUT":
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


file_address = "D:/ClassDocuments/Research/设计/流片/22_12_CHIP/Test/4T2R/signal_mapping.xlsx"
sheet_name = "访问阵列"
excel_generator(file_address, sheet_name)
