""" Create functions to manipulate ermineJ output """

import re
import os
import pandas as pd

from pygest import convenience


def tsvify_erminej_result(result_file):
    """ Read in results from ermineJ and write them back out with headers stripped. """

    converted = False  # Track whether we actually performed a conversion, or just found it already done
    tsv_file = result_file + "-tsv"
    if not os.path.isfile(tsv_file):
        converted = True
        with open(result_file, "r") as f_in:
            with open(tsv_file, "w") as f_out:
                for i, line in enumerate(f_in):
                    head_match = re.search('^#!\t', line)
                    if head_match:
                        f_out.write(line[3:].rstrip() + "\n")
                    data_match = re.search('^!\t', line)
                    if data_match:
                        f_out.write(line[2:].rstrip() + "\n")

    return tsv_file, converted


def describe_top_results(tsv_file, top_n=10):
    """ Read a tsv-based results file and print results legibly. """
    
    def describe_go_term(row):
        # import pdb; pdb.set_trace()
        return "{:<12}: {:<48} p{}".format(
            row['ID'], row['Name'],
            "={:0.5f}".format(row['CorrectedPvalue']) if row['CorrectedPvalue'] > 0.00001 else "<0.00001"
        )
    
    df = pd.read_csv(tsv_file, sep='\t').sort_values('CorrectedPvalue', ascending=True)
    df.loc[df['CorrectedPvalue'] < 0.05, :].iloc[:top_n, :].apply(lambda row: print(describe_go_term(row)), axis='columns')


def dataframe_from_erminej_results(result_file):
    """ Strip out extra stuff from ermineJ results, and load up the data as a dataframe. """

    tsv_file = result_file + ".stripped.tsv"
    if not os.path.isfile(tsv_file):
        with open(result_file, "r") as f_in:
            with open(tsv_file, "w") as f_out:
                for i, line in enumerate(f_in):
                    head_match = re.search('^#!\t', line)
                    if head_match:
                        f_out.write(line[3:].rstrip() + "\n")
                    data_match = re.search('^!\t', line)
                    if data_match:
                        f_out.write(line[2:].rstrip() + "\n")
                        
    df = pd.read_csv(tsv_file, sep="\t").sort_values('Pval', ascending=True)
    os.remove(tsv_file)
    
    return df


def p_real_v_shuffles(row):
    """ Calculate a p-value for each GO term, based on real terms outperforming shuffled terms.
        The "p" column is the ROC GO p-value for real data.
        Many "p_shuf_*" columns represent shuffled versions
        p = number of shuffled versions better than real / total comparisons
    """
    
    shuffled_columns = [col for col in row.index if "p_" in col]
    numerator = sum([row["p"] > row[p] for p in shuffled_columns])
    denominator = len(shuffled_columns)
    return pd.Series([numerator, denominator, numerator/denominator], index=["numerator", "denominator", "new_p", ])
        

def pygest_results_to_entrezid_ranks(pygest_file):
    """ Read a pygest result file, and write it as an entrezid-indexed rank file.
    """
    
    rank_file = pygest_file.replace(".tsv", ".entrez_rank")
    
    df = pd.read_csv(pygest_file, sep="\t").sort_values("seq", ascending=False)
    df['entrez_id'] = df['probe_id'].apply(convenience.map_pid_to_eid)
    df['rank'] = range(1, len(df) + 1)
    df[['entrez_id', 'rank']].to_csv(rank_file, sep="\t", index=False)
    
    return rank_file


def run_erminej_on_pygest_result(pygest_file, PYGEST_DATA="/data"):
    pass


def view_erminej_results_in_erminej(erminej_file, PYGEST_DATA="/data"):
    pass
