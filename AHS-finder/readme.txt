Acinetobacter sp. BIGb0196      g-Proteobacteria        WP_166782516
Acinetobacter sp. MYb10         g-Proteobacteria        WP_105712671
TenA family transcriptional regulator [Aquimarina aggregata] WP_066308905.1 TenA family transcriptional regulator [Aquimarina aggregata]
Tenacibaculum litoreum  Bacteroidetes   WP_125344594
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ python3 calculate_ai_ahs.py  -i similarity-btenA-VPI-5482-core-hits.out  -x intestinal-groups.yaml 
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ python3 calculate_ai_ahs.py  -i similarity-btenA-VPI-5482-core-hits.out  -x intestinal-groups-aqua-bacteroids.yaml  
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ pwd
../cheemaj/scratch/scratch-work/jitender/regis/RUN_AVP/AHS-finder
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ open .
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ 

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


(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat similarity-btenA-VPI-5482-core-hits-intestinal-groups_ai.out 
query name      donor   ingroup AI      HGTindex        query hits number       AHS     outg_pct
AAO78252.1      WP_066308905.1:8:44.860:4.87e-54:184    WP_011108665.1:1:100.000:0.0:514        -337.76051751422517     -330.0  47      561.0121773613256       95
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ cat similarity-btenA-VPI-5482-core-hits-intestinal-groups-aqua-bacteroids_ai.out 
query name      donor   ingroup AI      HGTindex        query hits number       AHS     outg_pct
AAO78252.1      WP_224431244.1:9:44.393:5.28e-54:184    WP_011108665.1:1:100.000:0.0:514        -337.84134967484886     -330.0  47      310.719412169753        95
(/Users/cheemaj/MM/myenv) N108628:AHS-finder cheemaj$ 

