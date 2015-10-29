#!/usr/bin/env python
import sys

## Usage python script.py {infile} {outfilename} {min_quality_to_replace_with_N}
### Assumptions
## File is sanger quality encoding
## That you have a sam file, and number of columns may not be consistent across lines

### Script purpose
## Trying to make a script that reads in the sam file, and replaces the bases with Ns if they are below a set quality

if len(sys.argv) != 4:
	sys.exit('Incorrect usage. Correct usage is: python script.py {infile} {outfilename} {min_quality_to_replace_with_N}')

print '\n\n*** STARTING ***\n\n'
print 'WARNING This script only works for sanger quality encoding. If you use with another encoding, it will output something that is wrong. i.e. it will not error out\n'

## Files
Infilename = sys.argv[1]
Infile = open(Infilename, 'rU')
Outfilename = sys.argv[2]
Outfile = open(Outfilename, 'w')

## Pre set variables
Min_quality = int(sys.argv[3])

### Function that converst the ascii character to the phred score then the quality score.
def convert_ascii_to_quality(ascii):
	phred = ord(ascii)
	quality_score = phred - 33
	return quality_score

## First print out the header lines and split the tab delimited file - col 9 = the read, 10 = quality scores.
## Then assuming your file is ok, convert the Read and ASCIIquality socres from a string to list, because strings are immutable
## Then send the ASCIIqscores to the function which will convert and return them as quality socres. You then iterate through the bases and quality scores at the same time position by position, and if the quality score in the ith position is < the specified threshold, you subsititute the BASE in ith position with an N. 	
## You then convert the list of strings and intergers to a single string.  
## Then assuming your file is ok, convert the Read and ASCIIquality socres from a string to list, because strings are immutable
## Then send the ASCIIqscores to the function which will convert and return them as quality socres. You then iterate through the bases and quality scores at the same time position by position, and if the quality score in the ith position is < the specified threshold, you subsititute the BASE in ith position with an N. 	
## You then convert the list of strings and intergers to a single string. 

###
# Main script
###

for Line in Infile:
	if Line.startswith('@'):
		Outfile.write(Line),  # Need the ,
	else:
		Cols=Line.strip('\n').split('\t')
		Num_cols = len(Cols)
		Read=Cols[9]
		ASCIIqscores=Cols[10]
		Qualityscores=[]
		 
		if len(Read) != len(ASCIIqscores):
			sys.exit("there is a problem, read and scores lenghts aren't the same, check columns above in the script are correct ")
		else:
			Bases = list(Read)
			ASCIIqscores = list(ASCIIqscores)
			for i in ASCIIqscores:
		 		Qualityscores.append(convert_ascii_to_quality(i))		
			Qualityscores = map(int, Qualityscores)
			for n,i in enumerate(Qualityscores):
				if Qualityscores[n] < Min_quality:
					Bases[n]="N"
			Bases = "".join(Bases)

			Outfile.write('\t'.join(Cols[0:9]) + '\t' + str(Bases) + '\t' + '\t'.join(Cols[10:Num_cols]) + '\n')

Outfile.close()

print '\n*** DONE ***\n\n'
