# import pandas as pd

# add labels to the zOTUs basing on the Taxonomy
# and COI sequence (Chimera, wrong_seq_length, unassigned)


def labels(table):
    table.insert(loc=3, column='label', value="empty")
    for row_no in range(0, len(table)):
        if len(table.iloc[row_no, 2].split(',')) == 7:  # check if taxonomy have 7 levels
            if table.iloc[row_no, 1] == "Chimera":
                table.loc[row_no, 'label'] = "Chimera"
            elif len(table.iloc[row_no, 4]) != 418 and len(table.iloc[row_no, 4]) != 415 and len(table.iloc[row_no, 4]) != 412:
                table.loc[row_no, 'label'] = "wrong_seq_length"
            elif table.iloc[row_no, 2].split(',')[2][:-6] == "Insecta":
                table.loc[row_no, 'label'] = "Insect"
            elif table.iloc[row_no, 2].split(',')[5][:-6] == "Wolbachia":
                table.loc[row_no, 'label'] = "Wolbachia"
            elif table.iloc[row_no, 2].split(',')[5][:-6] == "Rickettsia":
                table.loc[row_no, 'label'] = "Rickettsia"
            elif table.iloc[row_no, 2].split(',')[0][:-6] == "Bacteria":
                table.loc[row_no, 'label'] = "Other_Bacteria"
            elif table.iloc[row_no, 2].split(',')[1][:-6] == "Streptophyta":
                table.loc[row_no, 'label'] = "Plant"
            elif table.iloc[row_no, 2].split(',')[1][:-6] == "Basidiomycota" or table.iloc[row_no, 2].split(',')[1][:-6] == "Ascomycota":
                table.loc[row_no, 'label'] = "Fungus"
            elif table.iloc[row_no, 2].split(',')[2][:-6] == "Mammalia":
                table.loc[row_no, 'label'] = "Mammal"
            else:
                table.loc[row_no, 'label'] = "Other"
        else:
            if len(table.iloc[row_no, 4]) != 418 and len(table.iloc[row_no, 4]) != 415 and len(table.iloc[row_no, 4]) != 412:
                table.loc[row_no, 'label'] = "wrong_seq_length"
            else:
                table.loc[row_no, 'label'] = "unassigned"

    return table

# Adding some data to the output table (eg. sum of Wolbachia reads per library)


def labels_to_output(table, output_table):
    for col_name in list(table.columns)[6:]:
        zotu_group = table.groupby('label')[col_name].sum().reset_index()
        for label_name in list(zotu_group['label']):
            if label_name in list(output_table["label"]):
                # print(label_name)
                output_table.loc[output_table['label'] == label_name, col_name] = zotu_group.loc[zotu_group['label'] == label_name, col_name].item()
    return output_table
