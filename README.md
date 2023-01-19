# btenA
- Searching for optimal model of protein evolution using our core representatives protein alignment
- We ran the `ModelTest-NG` version v0.1.7, on the core proteins`data/prank-48_alignmt.fas` 
- The output files are in the folder `model-test-core` under this repo
- We ran ModelTest-NG version 0.1.7 on the alignment `prank-48_alignmt.fas`, we find the consensus model of evolution using both the optimal model using three criteria namely, Akaike information criterion (AIC), corrected Akaike information criterion (AICc), and the Bayesian information criterion (BIC) to be “WAG+I+G4”.


```bash
Modeltest-ng was called as follows: 

	WAG:	General matrix (Whelan and Goldman, 2001).
  +I : Rate heterogeneity across sites
  +G4: discrete Gamma model (Yang, 1994) with default 4 rate categories.

[cheemaj@NBI-HPC interactive model-test-core-48]$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/model-test-core-48
[cheemaj@NBI-HPC interactive model-test-core-48]$./modeltest-ng-static -i prank-48_alignmt.fas -d aa -p 16 
# optimal model found: 
                         Model         Score        Weight
----------------------------------------------------------
       BIC            WAG+I+G4    38901.9182        1.0000
       AIC            WAG+I+G4    38461.7530        1.0000
      AICc            WAG+I+G4    38488.7530        1.0000

[cheemaj@NBI-HPC interactive model-test-core]$ ls -1
prank-48_alignmt.fas
prank-48_alignmt.fas.ckp
prank-48_alignmt.fas.log
prank-48_alignmt.fas.tree
[cheemaj@NBI-HPC interactive model-test-core]$

```
# Building Maximum-likelihood(ML) tree with the Optimal model

- We built Maximum-likelihood(ML) tree `MLprank-48_alignment.phy.treefile` using `IQ-TREE multicore version 2.2.0`
- 1000 Bootstraps were generated and drawn on the optimal consensus tree `btenA/mltree-boostrapped/prank-48_alignment.phy.contree`
- Consensus bootstrapped tree was visualised with iTOL webserver `https://itol.embl.de/`
- The unrooted `btenA/mltree-boostrapped/ITOL/unrooted-ML-contree-core-circular.pdf` and the corresponding midpoint rooted tree is under `mid-point-rooted-itol/mid-rooted-ML-contree-core.nexus` and `mid-point-rooted-itol/mid-rooted-ML-contree-core-circular.pdf`

```
Command: /hpc-home/cheemaj/BUILD/IQTREE/iqtree-2.2.0-Linux/bin/iqtree2 -s prank-48_alignment.phy -m WAG+I+G4 -B 1000

Analysis results written to: 
  IQ-TREE report:                prank-48_alignment.phy.iqtree
  Maximum-likelihood tree:       prank-48_alignment.phy.treefile
  Likelihood distances:          prank-48_alignment.phy.mldist

Ultrafast bootstrap approximation results written to:
  Split support values:          prank-48_alignment.phy.splits.nex
  Consensus tree:                prank-48_alignment.phy.contree
  Screen log file:               prank-48_alignment.phy.log

# iTOL tree visualisation https://itol.embl.de/tree/1491552146571791674156084
[cheemaj@NBI-HPC interactive mltree-boostrapped]$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/mltree-boostrapped
[cheemaj@NBI-HPC interactive mltree-boostrapped]$
.
├── ITOL
│   ├── mid-point-rooted-itol
│   │   ├── mid-rooted-ML-contree-core-circular.pdf
│   │   ├── mid-rooted-ML-contree-core-circular.svg
│   │   ├── mid-rooted-ML-contree-core-newick.txt
│   │   ├── mid-rooted-ML-contree-core.nexus
│   │   ├── mid-rooted-ML-contree-core-rect.pdf
│   │   ├── mid-rooted-ML-contree-core-rect.svg
│   │   └── readme.txt
│   ├── prank-48_alignment.phy.contree
│   ├── readme.txt
│   ├── unrooted-ML-contree-core-circular.pdf
│   ├── unrooted-ML-contree-core-circular.svg
│   ├── unrooted-ML-contree-core-rect.pdf
│   └── unrooted-ML-contree-core-rect.svg
├── prank-48_alignment.phy
├── prank-48_alignment.phy.bionj
├── prank-48_alignment.phy.ckp.gz
├── prank-48_alignment.phy.contree
├── prank-48_alignment.phy.iqtree
├── prank-48_alignment.phy.log
├── prank-48_alignment.phy.mldist
├── prank-48_alignment.phy.splits.nex
├── prank-48_alignment.phy.treefile
└── readme.txt
  
```

# HGT check btenA 

- We start with a bteA protein sequence `btenA.fasta` and preforming a blastp (Protein-Protein BLAST version 2.9.0+) search against a remote `nr` database on 18.01.2022
- using a E cut-off 1e-5 we get 462 hits `data/similarity-btenA-VPI-5482.out`
- The equivalent hits are: AAO78252.1, 	WP_011108665.1
- Using the core proteins found in `data/prank-48_alignmt.fas` 
- Filter the hits using the core species table, `data/core-48-fixed-table.txt`

```bash
(/Users/cheemaj/MM/myenv) N108628:aux_scripts cheemaj$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/AVP/AvP-master/aux_scripts
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
##
[(/Users/cheemaj/MM/myenv) N108628:gen-core-fasta cheemaj$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/gen-core-fasta
(/Users/cheemaj/MM/myenv) N108628:gen-core-fasta cheemaj$ python extract-core-sequences.py  > run_log.txt
(/Users/cheemaj/MM/myenv) N108628:gen-core-fasta cheemaj$ python -V
Python 3.7.12
(/Users/cheemaj/MM/myenv) N108628:gen-core-fasta cheemaj$ python extract-core-sequences.py  > run_log.txt

#  using the core set filter out the lines to keep only the core protein hits: 
   "similarity-btenA-VPI-5482-core-hits.out"

# Construct the list of Ingroup and EG group yaml files:

# First the interstinal bacteroids config file
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat  intestinal-groups.yaml 
---
Ingroup:
 818: WP_011108665.1
 171549: WP_011108665.1
 226186: WP_011108665.1
EGP:
 106649: WP_166782516.1
 2587144: WP_166782516.1
 469: WP_166782516.1
 1827285: WP_105712671.1
 165179: WP_217327177.1
 674529: MCE8942323.1
 1871006: WP_195662386.1
 821: WP_229532965.1

# Running a modified script from the AvP tool: (https://github.com/GDKO/AvP/blob/master/aux_scripts/calculate_ai.py)
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ python3 calculate_ai_ahs.py  -i similarity-btenA-VPI-5482-core-hits.out  -x intestinal-groups-aqua-bacteroids.yaml 
# output
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat similarity-btenA-VPI-5482-core-hits-intestinal-groups_ai.out 
query name	donor	ingroup	AI	HGTindex	query hits number	AHS	outg_pct
AAO78252.1	WP_066308905.1:8:44.860:4.87e-54:184	WP_011108665.1:1:100.000:0.0:514	-337.76051751422517	-330.0	47	561.0121773613256	95
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ 

# second batch: interstinal bacteroids + Aquatic Bacteroidetes 
 (/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat  intestinal-groups-aqua-bacteroids.yaml 
---
Ingroup:
 818: WP_011108665.1
 171549: WP_011108665.1
 226186: WP_011108665.1
EGP:
 106649: WP_166782516.1
 2587144: WP_166782516.1
 469: WP_166782516.1
 1827285: WP_105712671.1
 165179: WP_217327177.1
 674529: MCE8942323.1
 1871006: WP_195662386.1
 821: WP_229532965.1
 1642818: WP_066308905.1
 321269: WP_125344594.1
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ 
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ python3 calculate_ai_ahs.py  -i similarity-btenA-VPI-5482-core-hits.out  -x intestinal-groups.yaml 
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat similarity-btenA-VPI-5482-core-hits-intestinal-groups-aqua-bacteroids_ai.out 
query name	donor	ingroup	AI	HGTindex	query hits number	AHS	outg_pct
AAO78252.1	WP_224431244.1:9:44.393:5.28e-54:184	WP_011108665.1:1:100.000:0.0:514	-337.84134967484886	-330.0	47	310.719412169753	95
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ 
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/RUN_AVP/AHS-finder
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ open .



```
