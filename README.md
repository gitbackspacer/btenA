# HGT check btenA 

- We start with a bteA protein sequence `btenA.fasta` and preforming a blastp (Protein-Protein BLAST version 2.9.0+) search against a remote `nr` database on 18.01.2022
- using a E cut-off 1e-5 we get 462 hits `data/similarity-btenA-VPI-5482.out`
- The equivalent hits are: AAO78252.1, 	WP_011108665.1
- Filter the hits using teh core species table, `data/core-48-fixed-table.txt`

```bash
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ pwd
/Volumes/Group-Scratch/Matthew-Hartley/cheemaj/scratch/scratch-work/jitender/regis/AVP/AvP-master/aux_scripts
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ 
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ which blastp
/Users/cheemaj/MM/myenv/bin/blastp
Protein-Protein BLAST 2.9.0+
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ blastp -remote -query btenA.fasta  -db nr -outfmt '6 std staxids' -seg no -evalue 1e-5 -out similarity-btenA-VPI-5482.out 
# number of hits
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ wc -l similarity-btenA-VPI-5482.out 
     462 similarity-btenA-VPI-5482.out
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ head similarity-btenA-VPI-5482.out 
AAO78252.1	WP_011108665.1	100.000	246	0	0	1	246	1	246	0.0	514	818;171549;226186
AAO78252.1	2A2M_A	97.551	245	6	0	2	246	14	258	1.38e-177	498	226186
AAO78252.1	WP_195662386.1	59.322	236	96	0	6	241	4	239	2.01e-97	295	1871006
AAO78252.1	WP_073346898.1	59.322	236	96	0	6	241	4	239	4.04e-97	295	1871006
AAO78252.1	MCD7962432.1	56.904	239	103	0	4	242	1	239	5.74e-97	294	2049048
AAO78252.1	WP_195406687.1	59.322	236	96	0	6	241	4	239	6.90e-97	294	1871006
AAO78252.1	WP_259020328.1	58.898	236	97	0	6	241	2	237	1.30e-96	293	818
AAO78252.1	CDA87108.1	59.322	236	96	0	6	241	4	239	1.89e-96	293	1262750
AAO78252.1	WP_227188819.1	58.475	236	98	0	6	241	2	237	6.20e-96	291	818
AAO78252.1	MBV4310778.1	58.475	236	98	0	6	241	4	239	6.63e-96	291	818
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ 
```
