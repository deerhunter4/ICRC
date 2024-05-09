import sys
import argparse


def parameters():
    parser = argparse.ArgumentParser(
        prog='Insect_COI_Reads_Classifier',
        description="""This program is written in Python.
        The program takes the insect COI zOTU (OTU) table and classifies
        reads into a few categories for each sample separately.
        As an output program gives a CSV file that contains a table of samples
        with reads divided into categories such as insect species barcode,
        Wolbachia, contaminants and potential_parasitoids
        (for a list of categories check the README.md file).""")
    # positional arguments
    parser.add_argument("path_to_input_file", metavar='zOTU_table.txt',
                        help="""path to the file containing zOTU table,
                        see README.md file in the GitHub repository""")
    # optional arguments
    parser.add_argument("-barcode", metavar='<barcode_treshold>', type=float,
                        help="barcode abundance treshold (default: 0.5)",
                        default=0.5)
    parser.add_argument("-secondary_barcode",
                        metavar='<secondary_barcode_treshold>',
                        type=float, help="""minimum OTU abundance treshold
                        to be considered as secondary barcode
                        (default: 0.20)""", default=0.20)
    parser.add_argument("-reads", metavar='<sample_reads_treshold>', type=int,
                        help="""minimum number o reads per library treshold
                        (default: 20)""", default=20)
    # if no arguments were given, printing the help message (args = "--help")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    return args


# get parameters
# param = parameters()
# print(param)
