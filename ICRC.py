from time import time
from args import parameters
import pandas as pd
from reads_treshold import reads_treshold
from labels import labels, labels_to_output
from output import output_table, output_fasta
from barcodes import proporcional_table, barcodes, barcode_species, barcode_to_output, satellite_genotypes
from contaminants import contam_and_parasitoids

start = time()

# get parameters
param = parameters()
print(param)

# read file
zotu = pd.read_csv(param.path_to_input_file, sep="\t")
zotu.dropna(axis=1, inplace=True)  # remove all columns with NaN

# drop samples (columns) with too low reads number
zotu = reads_treshold(zotu, param.reads)

# Labeling zOTUs in the zOTU table
zotu = labels(zotu)

# Preparing output table
output = output_table(zotu)

# adding data to output table
output = labels_to_output(zotu, output)

# create proporcional table, without Bacteria reads
zotu_proporcional = proporcional_table(zotu.loc[-zotu['Taxonomy'].str.contains('Bacteria')])

# finding barcode and secondary barcode for each library
barcode_list, barcode_dict = barcodes(zotu_proporcional)

# add barcode_species to the output table
output = barcode_species(zotu, zotu_proporcional, output, barcode_dict)

# add barcode and secondary barcode reads to the output table
output = barcode_to_output(zotu, zotu_proporcional, output, barcode_dict, param.barcode, param.secondary_barcode)

# finding satellite_genotypes and adding to the output
output = satellite_genotypes(zotu, output, barcode_dict)

# finding cross-contaminants and potential parasitoids
output = contam_and_parasitoids(zotu, output, barcode_dict, barcode_list)

# save barcodes as FASTA file
output_fasta(output)

# save output table into CSV file
# output.to_csv('reads_classification.csv', encoding='utf-8', index=False)
output.to_csv('reads_classification.txt', sep="\t", encoding='utf-8', index=False)

# count program run time
print(f"It took {time()-start} seconds.")
