import os
import pandas as pd
from typing import List


def read_blacklist(blacklist_file):
    blacklist: List[str] = []
    with open(blacklist_file, 'r') as file:
        blacklist = file.read().splitlines()

    result: List[str] = []
    for line in blacklist:
        result.append(line.strip())
    return result


def apply_blacklist(df, blacklist):
    if not blacklist:
        return df

    for domain in blacklist:
        df = df[df.domain != domain]
    return df


def merge_files(output_dir):
    '''Merges the output files into a single file.

    :param output_dir: str The directory where the output files are stored
    '''

    files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    if not files:
        return

    df = pd.concat([pd.read_csv(output_dir + f) for f in files])

    df = apply_blacklist(df, read_blacklist('domain_blacklist.txt'))

    df = df.drop_duplicates(subset='domain')

    df.to_csv(os.getcwd() + '/' + 'results.csv', index=False)
    for f in files:
        os.remove(output_dir + f)
