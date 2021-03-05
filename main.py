import pandas
import gooey


@Gooey(program_name="merge csv files")
def main():
    df_from_soesd = pandas.read_csv('soesd_transcript_file_3_4.csv')
    df_from_sis = pandas.read_csv('sis_q1_export.csv')
    pandas.merge(df_from_soesd, df_from_sis, on='Local Id', how='inner').to_csv('combined_data_q1.csv')


if __name__ == '__main__':
    main()
