import csv
from CSV_converter import CSV_converter


def combine_csv(file1_path, file2_path, output_path):
    # Read the contents of the first CSV file into a dictionary
    with open(file1_path, 'r', newline='') as file1:
        reader1 = csv.DictReader(file1)
        dict1 = {row['User-name']: row for row in reader1}

    # Read the contents of the second CSV file into a dictionary
    with open(file2_path, 'r', newline='') as file2:
        reader2 = csv.DictReader(file2)
        dict2 = {row['User-name']: row for row in reader2}

    # Merge the two dictionaries on the basis of the common keys
    merged_dict = {k: {**dict1.get(k, {}), **dict2.get(k, {})} for k in set(dict1) | set(dict2)}

    # Write the merged dictionary to a new CSV file
    with open(output_path, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(merged_dict.values())[0].keys())
        writer.writeheader()
        writer.writerows(merged_dict.values())


#CONVERT PROFILES JSON TO CSV
CSV_converter(r"C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\Profiles\Fakes\testprofiles.json",r"C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\testprofilescsv.csv")


# COMBINING PROFILES CSV AND BOTOMETER FILE
combine_csv(r"C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\testprofilescsv.csv",r"C:\\Users\\msabeeh.bee56mcs\\Desktop\\LATEST LATEST FYP\\newvenvName\\botometer_data.csv",r"C:\Users\msabeeh.bee56mcs\Desktop\LATEST LATEST FYP\newvenvName\testcsvprofiles&botometer.csv")


