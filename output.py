import pandas as pd

# Preparing output table


def output_table(table):
    col_names = list(table.columns)[6:]
    labels = [
        "barcode_species", "barcode", "second_barcode", "satellite_genotypes",
        "Wolbachia", "Rickettsia", "Other_Bacteria", "Plant", "Fungus",
        "Mammal", "cross_contaminants", "potential_parasitoid",
        "wrong_seq_length", "Chimera", "unassigned", "Other"]

    df = pd.DataFrame(index=range(0, 16), columns=col_names)
    df.insert(0, "label", labels, True)
    total = ["total"] + list(table.iloc[:, 6:].agg('sum'))
    df.loc[len(df)] = total
    return df
