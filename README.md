# replace_lowqualitybases
The python script replace_low_quality_bases_Ns_1.py takes a sanger quality encoded fastq file, and replaces low quality bases below a user specified threshold with an N.
This script was written for sanger quality encoding / phred + 33. It will not work for other encodings.

Usage:
python scriptname.py infilename outfilename minimum_qualityscore

For testing try testfile 3lines.sam
e.g. python replace_low_quality_bases_Ns_1.py 3lines.sam out.sam 35



