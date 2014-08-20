"""
When completed, this program should read in a set of "reads" in FASTA format,
and print out all the kmers. The kmer length k, and the filename of the file
containing the reads, must be supplied on the command-line. 

Usage:

    python find_kmers.py <reads-file> <k>
    
where <reads-file> and <k> are the parameters to use. For instance, to use
input data file input1.fa and k=3, run:

    python find_kmers.py input1.fa 3

"""

# This is starter code for you to modify for Challenge 1.
# You should edit the section below that is labelled "YOUR CODE HERE".
# You don't need to modify anything above that section.

# Import the Python libraries we'll need
import sys

# Get the command-line arguments and store them in variables reads_filename and k.
# The second argument will be a string like "3", so we convert it to an integer.
reads_filename = sys.argv[1]
k = int(sys.argv[2])

# Read the reads from the input file.
# Instead of writing out this part of the code, we could have used a Python
# library like biopython, which has pre-written functions to read FASTA files.
with open(reads_filename) as f:

    # Loop over the lines from the file, and store them as a list.
    # Strip the newlines off the end of each row.
    rows = []
    for row in f.readlines():
        rows.append( row.strip() )
    
    # Store our reads in a variable (a list) called reads.
    # Every second row of the file is a read.
    # The other rows are the read names, which we don't care about.
    # Here we start on the second row (index 1) and go to the end [1:],
    # with a step size of two [1::2]
    reads = rows[1::2]
    

####################### YOUR CODE HERE #######################

# You should replace the code below with your code to solve the challenge.
# Right now, the program just prints out each read, which isn't what we want.
#
# You'll need to use the variables which have been prepared by the code above:
#  - reads is a list containing strings (the input reads)
#  - k is an integer (the kmer length)

for read in reads:
    print read
