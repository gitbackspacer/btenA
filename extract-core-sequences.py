"""
 Extract a subset of sequence based on the core accesions listing

 input:
  - 'btenA-197-hits.fa'
  - 'core-48-fixed-table.txt'
 output: 
  'proteins-full-48-cores.fasta'
 
"""

import sys
import jitu


def load_locus_from_core(table_file = 'core-48-fixed-table.txt'):
    loci = []  # to keep an order 
    loci_flags = {} 
    with open(table_file) as inp:
         next(inp)
         for line in inp:
             A = line.strip().split('\t')
             if A:
                locus = A[3].strip()
                loci.append(locus)
                loci_flags[locus] = 0
    return loci, loci_flags


def match_locus_to_accession_id(ids, loci):
    for locus in loci:
        if locus in ids:
           return locus
    return None

def main():

    # load seuence: note we have three pairs of duplicate headers 194 unique
    sequence_headers, seqD = jitu.getSeqD('btenA-197-hits.fa')
    assert len(sequence_headers) == 197, 'Error: Check the table file it should have 197 records'   
    
    # load loci from table
    loci, loci_flags = load_locus_from_core(table_file = 'core-48-fixed-table.txt')
    assert len(loci) == len(loci_flags) == 48, 'Error: Check the table file it should have 48 records'   

    # generate the core fasta 
    core_ids = set()
    core_loci = {}
    with open('proteins-full-48-cores.fasta', 'w') as outf:
         for header in sequence_headers:
             ids = header[0]   
             locus = match_locus_to_accession_id(ids, loci)  
             if locus: 
                core_ids.add(ids) 
                loci_flags[locus] = 1
                core_loci[locus] = header  
                outf.write('>' + ids + '\n')
                outf.write(seqD[header] + '\n')

    assert len(core_ids) == 48, 'Error: Check the the faste file it should have 48 core records'   
    
    # make sure all core loci are found
    for locus in loci:
        assert loci_flags[locus], 'Locus not found or matche with the accession id: ' + locus

    print ('core_ids = ', core_ids)
    print ('core_loci = ', core_loci)

if __name__ == '__main__':
    main()


"""
output:
 core_ids  = ['WP_105712671.1', 'XP_027049566.1', 'PXF48067.1', 'XP_021377140.1', 'NCQ92070.1', 'XP_015760767.1', 'XP_003730491.2', 'WP_166782516.1', 'WP_229532965.1', 'XP_019617645.1', 'XP_015217116.1', 'XP_038153220.1', 'CAC5425173.1', 'WP_125344594.1', 'XP_043984437.1', 'WP_121897937.1', 'KTF92611.1', 'XP_045192634.1', 'XP_033749938.1', 'NP_001314821.1', 'XP_038050170.1', 'WP_078745630.1', 'WP_217327177.1', 'AIV52139.1', 'VDI43265.1', 'WP_066308905.1', 'WP_002614061.1', 'XP_043938478.1', 'XP_039608874.1', 'XP_001636921.2', 'XP_020903754.1', 'AAO78252.1', 'XP_028657201.2', 'KAH3819073.1', 'WP_195662386.1', 'XP_028412868.1', 'ETW93821.1', 'WP_242378554.1', 'EOR97517.1', 'XP_041096159.1', 'WP_224431244.1', 'XP_018610467.1', 'WP_012499220.1', 'WP_012909371.1', 'XP_022093498.1', 'XP_046871482.1', 'XP_005710530.1', 'MCE8942323.1'])
 core_loci = {'XP_038153220': ('XP_038153220.1', 'uncharacterized', 'protein', 'LOC119791271', '[Cyprinodon', 'tularosa]'), 'KTF92611': ('KTF92611.1', 'hypothetical', 'protein', 'cypCar_00003475', '[Cyprinus', 'carpio]'), 'WP_121897937': ('WP_121897937.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Rhodophyticola', 'porphyridii]'), 'KAH3819073': ('KAH3819073.1', 'hypothetical', 'protein', 'DPMN_120803', '[Dreissena', 'polymorpha]'), 'WP_242378554': ('WP_242378554.1', 'hypothetical', 'protein', '[Aeromonas', 'encheleia]'), 'XP_015760767': ('XP_015760767.1', 'PREDICTED:', 'uncharacterized', 'protein', 'LOC107339930', '[Acropora', 'digitifera]'), 'WP_066308905': ('WP_066308905.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Aquimarina', 'aggregata]'), 'NCQ92070': ('NCQ92070.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Microcystis', 'aeruginosa', 'LG13-13]'), 'WP_224431244': ('WP_224431244.1', 'hypothetical', 'protein', '[Aeromonas', 'rivuli]'), 'WP_229532965': ('WP_229532965.1', 'hypothetical', 'protein', '[Phocaeicola', 'vulgatus]'), 'XP_043938478': ('XP_043938478.1', 'uncharacterized', 'protein', 'LOC122811025', '[Protopterus', 'annectens]'), 'XP_020903754': ('XP_020903754.1', 'uncharacterized', 'protein', 'LOC110242137', '[Exaiptasia', 'diaphana]'), 'XP_001636921': ('XP_001636921.2', 'uncharacterized', 'protein', 'LOC5516928', '[Nematostella', 'vectensis]'), 'XP_028657201': ('XP_028657201.2', 'uncharacterized', 'protein', 'LOC114651558', '[Erpetoichthys', 'calabaricus]'), 'WP_217327177': ('WP_217327177.1', 'hypothetical', 'protein', '[Prevotella', 'copri]'), 'NP_001314821': ('NP_001314821.1', 'uncharacterized', 'protein', 'LOC100332348', 'precursor', '[Danio', 'rerio]'), 'VDI43265': ('VDI43265.1', 'Hypothetical', 'predicted', 'protein', '[Mytilus', 'galloprovincialis]'), 'XP_027049566': ('XP_027049566.1', 'uncharacterized', 'protein', 'LOC113677017', '[Pocillopora', 'damicornis]'), 'WP_002614061': ('WP_002614061.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Stigmatella', 'aurantiaca]'), 'XP_033749938': ('XP_033749938.1', 'uncharacterized', 'protein', 'LOC117334425', '[Pecten', 'maximus]'), 'XP_038050170': ('XP_038050170.1', 'uncharacterized', 'protein', 'LOC119723538', '[Patiria', 'miniata]'), 'XP_039608874': ('XP_039608874.1', 'uncharacterized', 'protein', 'LOC120528863', '[Polypterus', 'senegalus]'), 'XP_041096159': ('XP_041096159.1', 'uncharacterized', 'protein', 'LOC121307898', '[Polyodon', 'spathula]'), 'XP_021377140': ('XP_021377140.1', 'uncharacterized', 'protein', 'LOC110465552', '[Mizuhopecten', 'yessoensis]'), 'XP_022093498': ('XP_022093498.1', 'uncharacterized', 'protein', 'LOC110980809', '[Acanthaster', 'planci]'), 'WP_012909371': ('WP_012909371.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Pirellula', 'staleyi]'), 'WP_125344594': ('WP_125344594.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Tenacibaculum', 'litoreum]'), 'XP_019617645': ('XP_019617645.1', 'PREDICTED:', 'uncharacterized', 'protein', 'LOC109464968', '[Branchiostoma', 'belcheri]'), 'AAO78252': ('AAO78252.1', 'TenA', 'family', 'transcriptional', 'activator-like', 'protein', '[Bacteroides', 'thetaiotaomicron', 'VPI-5482]'), 'ETW93821': ('ETW93821.1', 'hypothetical', 'protein', 'ETSY1_37535', '[Candidatus', 'Entotheonella', 'factor]'), 'PXF48067': ('PXF48067.1', 'hypothetical', 'protein', 'BWQ96_02019', '[Gracilariopsis', 'chorda]'), 'XP_046871482': ('XP_046871482.1', 'uncharacterized', 'protein', 'LOC124463741', '[Hypomesus', 'transpacificus]'), 'AIV52139': ('AIV52139.1', 'TENA/THI-4/PQQC', 'family', 'protein', '[Burkholderia', 'pseudomallei', 'MSHR1153]'), 'WP_105712671': ('WP_105712671.1', 'hypothetical', 'protein', '[Acinetobacter', 'sp.', 'MYb10]'), 'WP_195662386': ('WP_195662386.1', 'hypothetical', 'protein', '[Bacteroides', 'congonensis]'), 'MCE8942323': ('MCE8942323.1', 'hypothetical', 'protein', '[Bacteroides', 'faecis]'), 'XP_005710530': ('XP_005710530.1', 'unnamed', 'protein', 'product', '[Chondrus', 'crispus]'), 'XP_003730491': ('XP_003730491.2', 'uncharacterized', 'protein', 'LOC100893025', '[Strongylocentrotus', 'purpuratus]'), 'WP_166782516': ('WP_166782516.1', 'MULTISPECIES:', 'hypothetical', 'protein', '[Acinetobacter]'), 'XP_015217116': ('XP_015217116.1', 'PREDICTED:', 'uncharacterized', 'protein', 'LOC107079203', '[Lepisosteus', 'oculatus]'), 'WP_012499220': ('WP_012499220.1', 'TenA', 'family', 'transcriptional', 'regulator', '[Chloroherpeton', 'thalassium]'), 'XP_028412868': ('XP_028412868.1', 'uncharacterized', 'protein', 'LOC114535758', '[Dendronephthya', 'gigantea]'), 'WP_078745630': ('WP_078745630.1', 'hypothetical', 'protein', '[Oceanospirillum', 'multiglobuliferum]'), 'XP_045192634': ('XP_045192634.1', 'uncharacterized', 'protein', 'LOC123548979', '[Mercenaria', 'mercenaria]'), 'XP_018610467': ('XP_018610467.1', 'uncharacterized', 'protein', 'LOC108935949', '[Scleropages', 'formosus]'), 'XP_043984437': ('XP_043984437.1', 'uncharacterized', 'protein', 'LOC122838113', '[Gambusia', 'affinis]'), 'CAC5425173': ('CAC5425173.1', 'unnamed', 'protein', 'product', '[Mytilus', 'coruscus]'), 'EOR97517': ('EOR97517.1', 'hypothetical', 'protein', 'C799_04352', '[Bacteroides', 'thetaiotaomicron', 'dnLKV9]')}

"""
