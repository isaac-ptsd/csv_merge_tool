import pandas
import os
import json

def csv_merge(file_1, file_2, column_name, merge_type="inner"):
    return pandas.merge(file_1, file_2, on=column_name, how=merge_type)


def main():
    conf = parse_args()

    print("Reading Files", flush=True)
    file_1_df = pandas.read_csv(conf.file_1)
    file_2_df = pandas.read_csv(conf.file_2)
    merged_df = csv_merge(file_1_df, file_2_df, conf.merge_on_column)

    out_path = os.path.join(conf.save_to, conf.file_name + '.csv')
    merged_df.to_csv(out_path)
    print(out_path, flush=True)


if __name__ == '__main__':
    main()