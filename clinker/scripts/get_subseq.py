python
from Bio import SeqIO
#index your gbk file as a dictionary
record_dict = SeqIO.index("Naganishia_friedmannii_Annotation_submitted_by_Jet_Propulsion_Laboratory,_California_Institute_of_Technology.gbk", "genbank")
#ID your chromosome of interest. This is the same as your contig ID
scaffold_11 = record_dict['scaffold_11']
#Find the specific start/stop you want to subset your gbk file. You can do this by ID'ing your gene start/stop for the region of interest using the gbk file.
scaffold_11_subseq = scaffold_11[302468:334699]
#write the output to a new gbk
SeqIO.write(scaffold_11_subseq, "Naganishia_friedmannii_chromosome_11.gbk", "gb")