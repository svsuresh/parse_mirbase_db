[miRBase](https://www.mirbase.org/download/) is miRNA source and allows the user to download the file as dat file. This file needs to be parsed to get details as tab separated values. This repo does that. Requirements are:
1. mirBase dat file
2. python3 installed
3. Biopython installed
4. Remove lines starting with "targets:pictar" from mirBase dat file
5. Run the command "python3 parse_miRNA_dat.py hsa miRNA1.dat test"
6. Multiple organisms are supported as 3 letter code (instead of hsa above, type mmu). If you do not furnish 3 letter code, program prints all the supported organisms if incorrect organism is provided
7. If output file path and name ("test" in step 5) are not provided, miRNAs are stored in "output.tsv" in same folder.
