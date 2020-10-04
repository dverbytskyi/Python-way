import csv
import pandas as pd

def merge_csv(csv_list, out_path):
    # build list with all filednames
    fieldnames = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            # extract fieldnames from file
            fn = csv.DictReader(input_csv).fieldnames
            # adding fieldnames to fieldnames list
            fieldnames.extend(item for item in fn if item not in fieldnames)

    # write data to output file based on field names
    with open(out_path, 'w', newline='') as output_csv:
        # passing list of fieldnames created before
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        # write first header row to output file
        writer.writeheader()
        # writing other rows
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

if __name__ == "__main__":
    files = ["class1.csv", "class2.csv"]
    merge_csv(files, 'class3.csv')