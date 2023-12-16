#!/usr/bin/bash -l
#SBATCH -p short -c 4 --mem 2G --job-name=BLASTN
#SBATCH --output=blastn.%A.log
module load ncbi-blast

CPUS=$SLURM_CPUS_ON_NODE
if [ ! -z $CPUS ]; then
    CPUS=1

blastn -query Yeast_chr2_ORFs.fa -db C_glabrata_ORFs.fasta \
-evalue 1e-5 -outfmt 6 -out yeastORF-vs-CglabrataORF.BLASTN.tab -num_threads $CPUS
