from Bio import SeqIO
import pandas as pd
import sys

records = SeqIO.parse(sys.argv[2], "embl")
records=list(records)

org_abbr=[]

for record in records:
    org_abbr.append(record.annotations['data_file_division'].lower())

org_abbr=sorted(set(org_abbr))

if sys.argv[1] in org_abbr:
    print(" Organism code found. Extracting miRNAs for ... ", sys.argv[1])
else:
    print (" Organism code", sys.argv[1]," not found.", "\n", "Choose one of the following organsims", "\n",', '.join(org_abbr))

record_subset = [record for record in records if record.annotations['data_file_division'].lower() == sys.argv[1]]

# record_subset = [record for record in records if record.annotations['data_file_division'].lower() == "hsa"]

# print(record_subset)

records_expanded=[]

for i in record_subset:
    # if "hsa" in i.annotations['data_file_division'].lower():
    if sys.argv[1] in i.annotations['data_file_division'].lower():
        org=i.description.rsplit(" ",2)[0]
        org_miR_name=i.name
        org_miR_id=i.id
        # print(i.dbxrefs)
        org_miR_dict=dict(j.split(':') for j in i.dbxrefs)
        org_miR_entrez=org_miR_dict.get('ENTREZGENE')
        org_miR_hgnc=org_miR_dict.get('HGNC')
        for j in i.features:
            if j.type=="miRNA":
                org_product=[j.qualifiers['product'] if 'product' in j.qualifiers else ""]
                org_accession=[j.qualifiers['accession'] if 'accession' in j.qualifiers else ""]
                records_expanded.append([org, "hsa", org_miR_name, org_miR_id, org_miR_entrez, org_miR_hgnc, *org_product[0], *org_accession[0]])

output = sys.argv[3] if len(sys.argv) > 3 else 'output'

# print(records_expanded)

col_names=['Organsim',sys.argv[1],'miRNA name','miRNA ID', 'ENTREZ Symbol', 'HGNC Symbol', 'miRNA product', 'miRNA accession']
pd.DataFrame(records_expanded, columns=col_names).to_csv(output+".tsv", sep="\t", index=0)