# Instructions

To set up and run these notebooks:

    git clone https://github.com/mfschmidt/schmidt_geconn.git
    cd schmidt_geconn
    pipenv install
    pipenv shell
    jupyter lab

# Directories (most have not yet been commited to git)

## Pre-processing (pre_processing)

### 01. filter_and_normalize_probes

Many python scripts used to reproduce [Aurina Arnatkeviciute's 2018 suggestions in Neuroimage](https://doi.org/10.1016/j.neuroimage.2019.01.011) for best practices in combining gene expression and other brain-mapped data. Some of her suggestions are compared with [Richiardi 2015's methods](https://doi.org/10.1126/science.1255905). Most of these have been ported to [PyGEST](https://github.com/mfschmidt/PyGEST), making these notebooks redundant and unnecessary.

- Filter probes:           ./pre_processing/filter_and_normalize_probes/02 - Filter probes.ipynb
- SRS adjust:              ./pre_processing/filter_and_normalize_probes/05 - SRS adjust.ipynb
    - compare SRS vs raw:  ./pre_processing/filter_and_normalize_probes/srs_differences/compare_srs_raw.ipynb

## Post-processing (post_processing)

### 02. probe_annotation

No code, data from online genomes

### ontology

The Main analyses discover ranked lists of genes by association with functional connectivity. To make sense of those genes, we run gene ontology on the ranked lists, resulting in new lists of components, mechanisms, or functions that are associated with genes overrepresented in our highly ranked lists. Gene ontology is performed by [ErmineJ](https://erminej.msl.ubc.ca/) and ErmineJ is now executed by [ge_data_manager](https://github.com/mfschmidt/ge_data_manager) on every result, including shuffles. We then determine which gene ontology results are more likely to be selected in real data than in shuffled.

- ./ontology/run_gene_ontology.ipynb can execute ermineJ from python. This was used to determine proper settings and execution parameters before porting this code into ge_data_manager. It is capable of downloading the most current ontology and annotation files prior to executing. It converts PyGEST result files into properly formatted ErmineJ input files. It can also execute the ErmineJ GUI afterward to explore results.
- ./ontology/collect_and_compare_gos.ipynb loops over all split half and split quarter results files, importing ErmineJ results and converting them to tsv files. That process takes over an hour, then all results are concatenated and used to generate p-values for each GO term. Finally, Kendall taus show how similar each set of gene lists is to each other, and to other sets.
- ./ontology/extract_go.ipynb is old and deprecated, replaced by collect_and_compare_gos.ipynb
- erminej.py contains support functions for re-use in handling GO.

## External comparisons (external)

### Spatial analyses of Richiardi data (spatial_richiardi)

### Compare our gene ontology lists to Fulcher's GSEA lists (fulcher_gsea)

## Other notebooks and things, not otherwise characterized

### 02. proximity_relationships

Both expression similarity and connectivity have relationships to proximity/distance. Code here explores those relationships and justifies our selection of a 16mm distance mask for optimizing Mantel correlations.

### 03. maps

Code to build maps linking probe_id, entrez_id, gene_symbol, etc.

### 04. gene_lists

Comparisions between our discovered genes and those reported in Gandal, et al. 2018, Wei, et al. 2019, Wang, et al. 2018, and Savage, et al. 2018.

- gandal_vs_schmidt.ipynb reads Gandal 2018 spreadsheet and saves relevant data to tsv files
- rank_p_values.ipynb calculates p-values for Schmidt-generated gene lists.

### spatial_richiardi

Created 11/9/2019 to explore spatial autocorrelation in Richiardi's 136 reported genes.

### overlap_data

Html output from sequential overlap analyses, dropping non-overlaps each iteration.

### debugging

Code snippets to help in reading and viewing cache files from the overlap plot generation in ge_data_manager

### ExpressionAndConnectivity

An unorganized disarray of old scripts, all dumped here to keep them in proximity of other associated scripts

