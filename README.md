# HGT check btenA 

- We start with a bteA protein sequence `btenA.fasta` and preforming a blastp (Protein-Protein BLAST version 2.9.0+) search against a remote `nr` database on 18.01.2022
- using a E cut-off 1e-5

```bash
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ pwd
/Volumes/Group-Scratch/Matthew-Hartley/cheemaj/scratch/scratch-work/jitender/regis/AVP/AvP-master/aux_scripts
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ 
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ which blastp
/Users/cheemaj/MM/myenv/bin/blastp
Protein-Protein BLAST 2.9.0+
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ blastp -remote -query btenA.fasta  -db nr -outfmt '6 std staxids' -seg no -evalue 1e-5 -out similarity-btenA-VPI-5482.out 

```
