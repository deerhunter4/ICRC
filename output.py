import pandas as pd


# Preparing output table
def output_table(table):
    col_names = list(table.columns)[6:]
    labels = [
        "zOTU", "OTU", "taxonomy", "sequence", "barcode_species",
        "barcode_%", "barcode", "second_barcode", "satellite_genotypes",
        "Wolbachia", "Rickettsia", "Other_Bacteria", "Plant", "Fungus",
        "Mammal", "cross_contaminants", "potential_parasitoid",
        "wrong_seq_length", "Chimera", "unassigned", "Other"]

    df = pd.DataFrame(index=range(0, 21), columns=col_names)
    df.insert(0, "label", labels, True)
    total = ["total"] + list(table.iloc[:, 6:].agg('sum'))
    df.loc[len(df)] = total
    return df


# output = pd.read_csv("reads_classifi?cation.txt", sep="\t")
# Preparing and saving barcode.fasta file
def output_fasta(output):
    with open("barcodes.fasta", "w") as file:
        for col_name in output.columns[1:].tolist():
            zotu = output[output['label'] == 'zOTU'][col_name].tolist()[0]
            otu = output[output['label'] == 'OTU'][col_name].tolist()[0]
            barcode_species = output[output['label'] == 'barcode_species'][col_name].tolist()[0]
            sequence = output[output['label'] == 'sequence'][col_name].tolist()[0]
            file.write(f">{col_name}_{zotu}_{otu}_{barcode_species}\n")
            file.write(f"{sequence}\n")

# output_fasta(output)

# output[output['label'] == 'zOTU']['GRE1673'].tolist()[0]
# output.loc[output['label'] == 'zOTU','GRE1673'].tolist()[0]