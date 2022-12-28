#!/usr/bin/python3

import os


s1 = "\subsection{XXalgebraNameXX}%\n\label{sec:XXalgebraNameXX}\n"
b1 = "XXalgebraNameXXYYalsoKnownYY appear XXappearXX~\cite{XXcitationsXX} and the number of non-isomorphic models from order 2 to order XXnumModelsXX is given in Table~\\ref{table:XXtlabelXX}.  XXExtraXX\n\n"

t1 = "\\begin{table}[!htb]\n    \\centering\n    \\caption{Number of XXalgebraNameXX}\n       \\begin{threeparttable}\n"
t2 = "          \\begin{tabular}{lXXrNumOrdersXX}\n         \\toprule\n"
tb1 = "        \\bottomrule \n       \\end{tabular} \n     \\end{threeparttable} \n     \\label{table:XXtlabelXX} \n \\end{table}"

extras = {'Near-ring': 'The numbers of near-rings up to order 7 were previously reported in the OEIS sequence~\seqnum{A305858}.  We extended this sequence to order 13.',
        'Involutory quandle': 'The numbers of involutory quandles up to order 10 were previously reported in the OEIS sequence~\seqnum{A178432}. We have added the number of of involutory quandles of order 11.'
        }

def read_csv(fn):
    """ takes the entry only if
        1. citation is present (i.e. x[2] is not empty)
        2. not the header row
    """
    with (open(fn)) as fp:
        entries = fp.readlines()
        entries = entries[1:]
        entries = [x.rstrip().split(',') for x in entries]
        entries = [x for x in entries if x[2]]
        for x in range(0, len(entries)):
            entries[x][0] = int(entries[x][0])
            entries[x][1] = entries[x][1].split(' ', 1)[1]
    return entries


def gen_section(fp, count, x):
    alg_name = x[1]
    citations = x[2]
    label = alg_name
    if x[3]:
        also_known = f", also known as {x[3]},"
    else:
        also_known = ""
    if x[4]:
        if "-" in x[4]:
            pg = "on pp. {x[4]} of"
        else:
            pg = f"on p. {x[4]} of"
    else:
        pg = "in"
    seq = x[5:]
    seq = [int(x) for x in seq if x]
    max_order = len(seq) + 1
    rows = ['{:,} '.format(c) for c in seq]

    boiler1 = f"{s1}{b1}"
    boiler1 = boiler1.replace("XXalgebraNameXX", alg_name)
    boiler1 = boiler1.replace("XXappearXX", pg)
    boiler1 = boiler1.replace("YYalsoKnownYY", also_known)
    boiler1 = boiler1.replace("XXnumModelsXX", str(max_order))
    boiler1 = boiler1.replace("XXcitationsXX", citations)
    boiler1 = boiler1.replace("XXtlabelXX", label)
    boiler1 = boiler1.replace("XXExtraXX", extras.get(alg_name, ''))
    boiler2 = f"{t1}{t2}"
    boiler2 = boiler2.replace("XXrNumOrdersXX", 'r'*(max_order-1))
    boiler2 = boiler2.replace("XXalgebraNameXX", alg_name)
    boiler3 = f"{tb1}"
    boiler3 = boiler3.replace("XXtlabelXX", label)
    # print(boiler1)
    # print(boiler2)
    fp.write(boiler1)
    fp.write(boiler2)
    fp.write("        Order: & ")
    fp.write(" & ".join([str(x) for x in range(2, max_order+1)]) + " \\\\" + os.linesep)
    fp.write(f"        \\cmidrule{{1-{max_order}}}" + os.linesep)
    fp.write("        \\#Models: & ")
    fp.write(" & ".join(rows) + " \\\\" + os.linesep)
    fp.write(boiler3 + os.linesep + os.linesep)
    return max_order 


def run(csv, latexfn):
    algs = read_csv(csv)
    with open(latexfn, "w") as fp:
        for count, x in enumerate(algs):
            gen_section(fp, count, x)

    return len(algs)


if __name__ == '__main__':
    num = run("algebras.csv", "sequences.tex")
    print(num)

