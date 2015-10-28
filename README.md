# replace_lowqualitybases
This script takes a sanger quality encoded fastq file, and replaces low quality bases below a user specified threshold with an N.
This script was written for, and is only suitable for, sanger quality encoded fastq ONLY.

Usage:
python scriptname.py <infilename> <outfilename> <minimum_qualityscore>
e.g. python replace_low_quality_bases_Ns_1.py 3lines.sam out.sam 20

Test samfile is provided.

