# import pandas as pd


# prepare proporcional table
def proporcional_table(table):
    proporcional_table = table.copy()  # make independent copy of a dataframe
    proporcional_table[proporcional_table.columns[5:]] = proporcional_table[proporcional_table.columns[5:]].astype('float64')
    proporcional_table.iloc[:, 5:] = proporcional_table.iloc[:, 5:].apply(lambda col: col / sum(col))
    return proporcional_table


# finding barcode and secondary barcode for each library
def barcodes(proporcional_table):
    barcode_list = []
    barcode_dict = {}
    proporcional_table_insect = proporcional_table[proporcional_table['label'] != "Bacteria"]
    for col_no in range(6, len(proporcional_table_insect.iloc[1, :])):
        two_max_row_id = proporcional_table_insect.iloc[:, col_no].nlargest(2).index.tolist()
        barcode_dict[proporcional_table_insect.columns[col_no]] = two_max_row_id
        if proporcional_table.loc[two_max_row_id[0], 'Taxonomy'] != 'unassigned':
            barcode_species = proporcional_table.loc[two_max_row_id[0], 'Taxonomy'].split(',')[5][:-6]  # extract barcode genus name
            barcode_list.append(barcode_species)

    barcode_list = list(set(barcode_list))
    return barcode_list, barcode_dict


# add barcode_species to the output table
def barcode_species(table, proporcional_table, output, barcode_dict):
    for col_name in table.columns[6:].tolist():
        if table.loc[barcode_dict[col_name][0], [col_name]].tolist()[0] != 0:
            if table.loc[barcode_dict[col_name][0], 'Taxonomy'] != 'unassigned':
                barcode_species = table.iloc[barcode_dict[col_name][0], 2].split(',')[6]
            else:
                barcode_species = table.iloc[barcode_dict[col_name][0], 2]
            output.loc[output['label'] == "barcode_species", [col_name]] = barcode_species
            output.loc[output['label'] == "zOTU", [col_name]] = table.iloc[barcode_dict[col_name][0], 0]
            output.loc[output['label'] == "OTU", [col_name]] = table.iloc[barcode_dict[col_name][0], 1]
            output.loc[output['label'] == "taxonomy", [col_name]] = table.iloc[barcode_dict[col_name][0], 2]
            output.loc[output['label'] == "sequence", [col_name]] = table.iloc[barcode_dict[col_name][0], 4]
            output.loc[output['label'] == "barcode_%", [col_name]] = proporcional_table.loc[barcode_dict[col_name][0], [col_name]].tolist()[0]
        else:
            output.loc[output['label'] == "barcode_species", [col_name]] = "unassigned"
            print(output.loc[output['label'] == "barcode_species", [col_name]])
    return output


# add barcode and secondary barcode reads to the output table
def barcode_to_output(table, proporcional_table, output, barcode_dict, barcode_treshold, second_treshold):
    for col_name in table.columns[6:].tolist():
        max = proporcional_table.loc[barcode_dict[col_name][0], [col_name]].tolist()[0]
        second = proporcional_table.loc[barcode_dict[col_name][1], [col_name]].tolist()[0]
        if table.loc[barcode_dict[col_name][0], 'Taxonomy'] != 'unassigned':
            barcode_genus = table.iloc[barcode_dict[col_name][0], 2].split(',')[5][:-6]
            output.loc[output['label'] == "barcode", [col_name]] = table.loc[barcode_dict[col_name][0], [col_name]].tolist()[0]
        else:
            barcode_genus = table.iloc[barcode_dict[col_name][0], 2]
            output.loc[output['label'] == "barcode", [col_name]] = 0
        if table.loc[barcode_dict[col_name][1], 'Taxonomy'] != 'unassigned':
            second_genus = table.iloc[barcode_dict[col_name][1], 2].split(',')[5][:-6]
        else:
            second_genus = table.iloc[barcode_dict[col_name][1], 2]
        if max < barcode_treshold:
            print(f"Most abundand Insect zOTU in sample {col_name} accounts for less than {barcode_treshold*100}% of reads")
        if second > second_treshold and second_genus == barcode_genus:
            output.loc[output['label'] == "second_barcode", [col_name]] = table.loc[barcode_dict[col_name][1], [col_name]].tolist()[0]
        else:
            output.loc[output['label'] == "second_barcode", [col_name]] = 0
            barcode_dict[col_name] = [barcode_dict[col_name][0]]
    return output


# finding satellite_genotypes and adding to the output
def satellite_genotypes(table, output, barcode_dict):
    table_insect = table.loc[table['label'] == 'Insect', :]
    for col_name in table.columns[6:].tolist():
        if table.loc[barcode_dict[col_name][0], 'Taxonomy'] != 'unassigned':
            barcode_genus = table.iloc[barcode_dict[col_name][0], 2].split(',')[5][:-6]
            zotu_satellite = table_insect.loc[table_insect['Taxonomy'].str.contains(barcode_genus)]
            zotu_satellite = zotu_satellite.drop(barcode_dict[col_name])
            output.loc[output['label'] == "satellite_genotypes", col_name] = zotu_satellite[col_name].sum()
    return output
