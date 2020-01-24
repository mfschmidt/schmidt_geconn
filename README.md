# Instructions

To set up and run these notebooks:

    git clone https://github.com/mfschmidt/schmidt_geconn.git
    cd schmidt_geconn
    pipenv install
    pipenv shell
    jupyter lab

# Directories (most have not yet been commited to git)

## 01. filter_and_normalize_probes

Many python scripts used to reproduce Aurina Arnatkeviciute's 2018 suggestions in Neuroimage for best practices in combining gene expression and other brain-mapped data. Some of her suggestions are compared with Richiardi 2015's methods.

## 02. proximity_relationships

Both expression similarity and connectivity have relationships to proximity/distance. Code here explores those relationships and justifies our selection of a 16mm distance mask for optimizing Mantel correlations.

## 03. maps

Code to build maps linking probe_id, entrez_id, gene_symbol, etc.

## 04. gene_lists

Comparisions between our discovered genes and those reported in Gandal, et al. 2018, Wei, et al. 2019, Wang, et al. 2018, and Savage, et al. 2018.

- gandal_vs_schmidt.ipynb reads Gandal 2018 spreadsheet and saves relevant data to tsv files
- rank_p_values.ipynb calculates p-values for Schmidt-generated gene lists.

## spatial_richiardi

Created 11/9/2019 to explore spatial autocorrelation in Richiardi's 136 reported genes.

## ontology

Gene ontology outputs, raw with no code to assist in their analysis.

## overlap_data

Html output from sequential overlap analyses, dropping non-overlaps each iteration.

## probe_annotation

No code, data from online genomes

## debugging

Code snippets to help in reading and viewing cache files from the overlap plot generation in ge_data_manager

## ExpressionAndConnectivity

An unorganized disarray of old scripts, all dumped here to keep them in proximity of other associated scripts

