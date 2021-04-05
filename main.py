import pandas
import os
import json
from gooey import Gooey, GooeyParser


def parse_args():
    stored_args = {}

    # get the script name without the extension & use it to build the json filename
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.json".format(script_name)

    # Read in the prior arguments as a dictionary
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = json.load(data_file)
    parser = GooeyParser(description='Will merge two csv files into one, using the user provided column name.')
    parser.add_argument('file_1',
                        action='store',
                        default=stored_args.get('file_1'),
                        widget='FileChooser',
                        help="Choose a .csv file")
    parser.add_argument('file_2',
                        action='store',
                        default=stored_args.get('file_2'),
                        widget='FileChooser',
                        help="Choose a .csv file")
    parser.add_argument('save_to',
                        action='store',
                        widget='DirChooser',
                        default=stored_args.get('save_to'),
                        help="Output directory to save the combined .csv files")
    parser.add_argument('file_name',
                        action='store',
                        default=stored_args.get('file_name'),
                        help="Name your new file")
    parser.add_argument('merge_on_column',
                        action='store',
                        default=stored_args.get('merge_on_column'),
                        help="enter the column name to merge on")
    # parser.add_argument('merge_type',
    #                     action='store',
    #                     default=stored_args.get('merge_type'),
    #                     choices=["inner", "left", "right", "outer"],
    #                     help="enter the merge_type")
    args = parser.parse_args()
    # Store the values of the arguments so we have them next time we run
    with open(args_file, 'w') as data_file:
        # Using vars(args) returns the data as a dictionary
        json.dump(vars(args), data_file)
    return args


def csv_merge(file_1, file_2, column_name, merge_type="inner"):
    return pandas.merge(file_1, file_2, on=column_name, how=merge_type)


@Gooey(program_name="merge csv files")
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
