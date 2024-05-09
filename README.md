# Insect_COI_Reads_Classifier [ICRC]

This program is written in Python.The program takes the insect COI zOTU (OTU) table and classifies reads into a few categories for each sample separately. As an output program gives a txt file that contains a table of samples with reads divided into 15 categories (for details check example belowe).

**Requirements:**

Unix environment, Python 3.12.1

**Usage:**

`ICRC.py input_file.txt`  
`ICRC.py otu_table.txt -barcode 0.8 -reads 50`  
`ICRC.py input_file_2.txt - secondaty_barcode -0.15 -reads 10`

**Optional arguments:**

**-barcode** - Minimum abundance treshold that zOTU has to have to be considered as most abundand zOTU (default: 0.5). If the most abundand Insect zOTU in sample accounts belowe the treshold value the warning message will be printed on the screen.  
**-secondary_barcode** - Minimum OTU abundance treshold to be considered as secondary barcode (default: 0.20).  
**-reads** - Minimum number of reads per library/sample to be included in the output files (default: 20).

**Example of input file:**

Input is a COI zOTU (OTU) table text file (tab delimited).  
[test_zotu_table_expanded.txt]

OTU_ID | OTU_assignment | Taxonomy | Sequence | Total | GRE2059 | GRE2091 | GRE1351 | GRE0882
-------|----------------|----------|----------|-------|---------|---------|---------|--------
Zotu1 | otu1 | Eukaryota(1.00),Arthropoda(1.00),(...) | AATAAATAATATAAGTT(...) | 78218 | 2126 | 0 | 0 | 2  
Zotu2 | otu1 | Eukaryota(1.00),Arthropoda(1.00),(...) | TATGAATAATTTAAGTT(...) | 68883 | 0 | 71 | 0 | 68812  

**Example of output file:**

Output is [reads_classification.txt] file (tab delimited).  

label | GRE2059 | GRE2091 | GRE1351 | GRE0882
------|---------|---------|---------|--------
barcode_species | Orthocladius_roussellae(1.00) | Bombus_hyperboreus(1.00) | Tokunagaia_rectangularis(1.00) | Spilogona_dorsata(1.00)
barcode | 42240 | 59784 | 43485 | 1976
second_barcode | 0 | 0 | 0 | 0
satellite_genotypes | 0 | 3415 | 0 | 0
Wolbachia | 0 | 0 | 0 | 1619
Rickettsia | 0 | 0 | 0 | 0
Other_Bacteria |  |  |  |
Plant | 0 | 65 | 0 | 0
Fungus | 0 | 0 | 0 | 4
Mammal | 0 | 0 | 0 | 0
cross_contaminants | 0 | 447 | 0 | 0
potential_parasitoid | 0 | 258 | 0 | 4
wrong_seq_length | 0 | 25 | 14 | 2
Chimera | 0 | 0 | 0 | 0
unassigned | 0 | 0 | 0 | 0
Other | 0 | 782 | 0 | 0
total | 42240 | 64776 | 43499 | 3605

**Output file labels explanation**

* barcode_species - species name of most abundand ZOTU (but see belowe).
* barcode - number of reads of most abundant Insect zOTU in the library/sample. Number of reads are always shown, even if abundance is belowe treshold.
* second_barcode - number of reads of second most abundant Insect zOTU in the library/sample that belong to the same genus as the barcode and its abundance is higher than the treshold.
* satellite_genotypes - sum number of reads of reamaning zOTUs belonging to the same genus as the barcode.
* Wolbachia - sum number of reads of Wolbachia zOTUs.
* Rickettsia - sum number of reads of Rickettsia zOTUs.
* Other_Bacteria - sum number of reads of Bacteria zOTUs except the two above.
* Plant - sum number of reads of Streptophyta clad zOTUs.
* Fungus - sum number of reads of Basidiomycota and Ascomycota clad zOTUs.
* Mammal - sum number of reads of Mammalian zOTUs.
* cross_contaminants - sum number of reads belonging to any of the identified barcode species except the one from this library.
* potential_parasitoid - sum number of reads belonging to Insect zOTUs but not belonging to any of the identified barcode species.
* wrong_seq_length - sum number of reads of all zOTUs which sequence length is not different from 418bp, 415bp and 412bp. This label combine all zOTU reads that normally would belong to any other label (excep Chimera).
* Chimera - sum number of reads of zOTUs marked as chmieras
* unassigned - sum number of reads of ZOTUs for which taxonomy was not resolved. In many cases blasting sequence on NCBI site might give valid result.
* Other - sum number of reads of any left ZOTUs. Eg. Arachnida.
* total - this number is taken from oryginal table, so if reads from all other labels do not count to number in this row something went wrong!

*if a label do not have any reads number (even 0) it mean that in any zOTU in any sample/library was fitting this category  
*
