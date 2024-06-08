# import pandas as pd


# finding cross-contaminants and potential parasitoids
def contam_and_parasitoids(table, output, barcode_dict, barcode_list):
    table_insect = table.loc[table['label'] == 'Insect', :]
    for col_name in table.columns[6:].tolist():
        contaminants_count = 0
        parasitoids_count = 0
        if table.loc[barcode_dict[col_name][0], 'Taxonomy'] != 'unassigned':
            barcode_genus = table.iloc[barcode_dict[col_name][0], 2].split(',')[5][:-6]
        else:
            barcode_genus = table.iloc[barcode_dict[col_name][0], 2]
        not_barcode_insect = table_insect[-table_insect['Taxonomy'].str.contains(barcode_genus)]
        for row_no in not_barcode_insect.index.tolist():
            if not_barcode_insect.loc[row_no, 'Taxonomy'].split(',')[5][:-6] in barcode_list:
                contaminants_count += not_barcode_insect.loc[row_no, col_name]
            else:
                parasitoids_count += not_barcode_insect.loc[row_no, col_name]
        output.loc[output['label'] == "cross_contaminants", col_name] = contaminants_count
        output.loc[output['label'] == "potential_parasitoid", col_name] = parasitoids_count
    return output
