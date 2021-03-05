import pandas
import os
import json
from gooey import Gooey, GooeyParser


@Gooey(program_name="merge csv files")
def parse_args():
    stored_args = {}

    # get the script name without the extension & use it to build the json filename
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.json".format(script_name)

    # Read in the prior arguments as a dictionary
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = json.load(data_file)
    parser = GooeyParser(description='Merge')
    parser.add_argument('File 1',
                        action='store',
                        default=stored_args.get('data_directory'),
                        widget='DirChooser',
                        help="Choose a csv file")
    parser.add_argument('File 2',
                        action='store',
                        default=stored_args.get('data_directory'),
                        widget='DirChooser',
                        help="Choose a csv file")
    parser.add_argument('output_directory',
                        action='store',
                        widget='DirChooser',
                        default=stored_args.get('output_directory'),
                        help="Output directory to save the combined .xlsx files")
    parser.add_argument('file_name',
                        action='store',
                        default=stored_args.get('file_name'),
                        help="Name your new file")
    args = parser.parse_args()
    # Store the values of the arguments so we have them next time we run
    with open(args_file, 'w') as data_file:
        # Using vars(args) returns the data as a dictionary
        json.dump(vars(args), data_file)
    return args


def csv_merge(file_1, file_2, file_name):
    file_1_df = pandas.read_csv(file_1)
    file_2_df = pandas.read_csv(file_2)
    pandas.merge(file_1_df, file_2_df, on='Local Id', how='inner').to_csv(file_name)


def main():
    conf = parse_args()
    print("Reading Files", flush=True)
    df_from_soesd = pandas.read_csv('soesd_transcript_file_3_4.csv')
    df_from_sis = pandas.read_csv('sis_q1_export.csv')
    pandas.merge(df_from_soesd, df_from_sis, on='Local Id', how='inner').to_csv('combined_data_q1.csv')


if __name__ == '__main__':
    main()
