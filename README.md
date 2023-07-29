[miRBase](https://www.mirbase.org/download/) is miRNA source and allows the user to download the file as dat file. This file needs to be parsed to get details as tab separated values. This repo does that. Requirements are:
1. mirBase dat file
2. python3 installed
3. Biopython installed
4. Remove lines starting with "targets:pictar" from mirBase dat file
5. Run the command "python3 parse_miRNA_dat.py hsa miRNA1.dat test"
6. Multiple organisms are supported as 3 letter code (instead of hsa above, type mmu). If you do not furnish 3 letter code, program prints all the supported organisms if incorrect organism is provided
7. If output file path and name ("test" in step 5) are not provided, miRNAs are stored in "output.tsv" in same folder.

Output would be:

| Organsim	| hsa	| miRNA name	| miRNA ID	| ENTREZ Symbol	| HGNC Symbol	| miRNA product	| miRNA accession|
| :---:   | :---: | :---: | :---:   | :---: | :---: | :---:   | :---: |
| Homo sapiens	| hsa	| hsa-let-7a-1	| MI0000060	| 406881	| 31476	| hsa-let-7a-5p	| MIMAT0000062 |
| Homo sapiens	| hsa	| hsa-let-7a-1	| MI0000060	| 406881	| 31476	| hsa-let-7a-3p	| MIMAT0004481 |
| Homo sapiens	| hsa	| hsa-let-7a-2	| MI0000061	| 406882	| 31477	| hsa-let-7a-5p	| MIMAT0000062 |
| Homo sapiens	| hsa	| hsa-let-7a-2	| MI0000061	| 406882	| 31477	| hsa-let-7a-2-3p	| MIMAT0010195 |
| Homo sapiens	| hsa	| hsa-let-7a-3	| MI0000062	| 406883	| 31478	| hsa-let-7a-5p	| MIMAT0000062 |
| Homo sapiens	| hsa	| hsa-let-7a-3	| MI0000062	| 406883	| 31478	| hsa-let-7a-3p	| MIMAT0004481 |
| Homo sapiens	| hsa	| hsa-let-7b	| MI0000063	| 406884	| 31479	| hsa-let-7b-5p	| MIMAT0000063 |
| Homo sapiens	| hsa	| hsa-let-7b	| MI0000063	| 406884	| 31479	| hsa-let-7b-3p	| MIMAT0004482 |
| Homo sapiens	| hsa	| hsa-let-7c	| MI0000064	| 406885	| 31480	| hsa-let-7c-5p	| MIMAT0000064 |
