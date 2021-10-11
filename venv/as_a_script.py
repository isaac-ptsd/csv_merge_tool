import pandas
import os


def csv_merge(file_1, file_2, column_name, merge_type="inner"):
    return pandas.merge(file_1, file_2, on=column_name, how=merge_type)


def main():
    file_1 = input("Enter file path 1: ").replace("\\", "\\")
    file_2 = input("Enter file path 2: ").replace("\\", "\\")
    file_name = input("Name your file: ")
    save_to = input("Enter the path to a save location: ").replace("\\", "\\")
    merge_on_column = input("Enter a column name to merge on: ")

    file_1_df = pandas.read_csv(file_1)
    file_2_df = pandas.read_csv(file_2)
    merged_df = csv_merge(file_1_df, file_2_df, merge_on_column)

    out_path = os.path.join(save_to, file_name + '.csv')
    merged_df.to_csv(out_path)


if __name__ == '__main__':
    main()
