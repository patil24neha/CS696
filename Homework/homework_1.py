"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    comp_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    comp_string = ''
    for i in dna:
        comp_string += comp_dict[i]
    return comp_string

print(fast_complement("ATCGCT"))

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    return s[:start] + s[stop+1:]

print(remove_interval('ABCDEFGHI', 2, 5))

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    outList = []
    for i in range(0, len(s) - k + 1):
        outList.append(s[i:i + k])
    return outList

print(kmer_list('CTTTAAGGAG', 2))

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    outSet = set()
    for i in range(0, len(s) - k + 1):
        outSet.add(s[i:i + k])
    return outSet

print(kmer_set('CTTTAAGGAG', 2))


def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    outDict = {}
    for i in range(0, len(s) - k + 1):
        if s[i:i + k] in outDict:
            outDict[s[i:i + k]] += 1
        else:
            outDict[s[i:i + k]] = 1
    return outDict

print(kmer_dict('CTTTAAGGAG', 2))


# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name, 'r') as x:
        lines = x.readlines()[:10]
        for line in lines:
            print (line)

head('input.txt')

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    lines = ''
    with open(file_name, 'r') as x:
        lines = x.readlines()[-10:]
        for line in lines:
            print (line)

tail('input.txt')

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    i = 1
    lines = ''
    with open(file_name, 'r') as x:
        for line in x.readlines():
            if i % 2 == 0:
                print(line)
            i += 1

print_even('input.txt')

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    with open(file_name, 'r') as x:
        tuple = []
        line = ""
        for line in x.readlines():
            if line[-1] == '\n':
                line = line[:-1]
            tuple.append(line.split(","))
        return tuple

print(csv_list('input.csv'))

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    with open(file_name, 'r') as x:
        col = []
        line = ""
        for line in x.readlines():
            if line[-1] == '\n':
                line = line[:-1]
            col.append(line.split(",")[column])
        return col

print(get_csv_column('input.csv',1))


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    seq_list = []
    seqs = ''
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                if len(seq) == 0:
                    continue
                x = seq.split('\n', 1)
                sequence = x[1].replace('\n', '')
                seq_list.append(sequence)
            except:
                print('error')
        return seq_list

print(fasta_seqs('input.fasta'))

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    header_list = []
    headers = ''
    with open(file_name, 'r') as infile:
        text = infile.read()
        headers = text.split('>')
        for header in headers:
            try:
                if len(header) == 0:
                    continue
                x = header.split('\n', 1)
                header = x[0]
                header_list.append(header)
            except:
                print('error')
        return header_list

print(fasta_headers('input.fasta'))

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    my_dict = {}
    with open(file_name, 'r') as file:
        text = file.read()
        seqs = text.split('>')
        for seq in seqs:
            try:
                if len(seq) == 0:
                    continue
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                my_dict[header] = sequence
            except:
                    print('error')
        return my_dict

print(fasta_dict('input.fasta'))

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    new_fname = ''
    if not file_name.endswith('.fastq'):
        print('Filename is invalid : ' + file_name)
    else:
        if new_name is None:
            new_fname = file_name.replace('.fastq','.fasta')
        else:
            new_fname = new_name
        try:
            with open(file_name, 'r') as infile:
                text = infile.read()
                seqs = text.split('@')
                new_file = open(new_fname, 'w')
                for seq in seqs:
                    try:
                        if len(seq) == 0:
                            continue
                        x = seq.split('\n')
                        header = x[0]
                        sequence = x[1]
                        new_file.write('>' + header + '\n' + sequence + '\n')
                    except:
                        print('Error')
                        continue
                new_file.close()
        except:
            print('Error in input file: ' + file_name)
    return

fastq_to_fasta('proper_fastq.fastq')
fastq_to_fasta('proper_fastq.fastq','new1.fasta')

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return "".join([comp_dict[base] for base in reversed(dna)])

print(reverse_complement('CTAGT'))

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    return dna.replace('T', 'U')

print(transcribe('CTAGAC'))

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    ans = ''
    try:
        for i in range(0, len(rna), 3):
            compo = RNA_CODON_TABLE[rna[i:i + 3]]
            if compo == '*':
                break
            ans += compo
    except KeyError:
        pass
    return ans

print(translate('CUAGGCGGUAA'))

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    frame_list = []
    frame_list.append(dna)
    frame_list.append(dna[1:-2])
    frame_list.append(dna[2:-1])

    comp_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    revComp = ''
    for i in reversed(dna):
        revComp += comp_dict[i]

    frame_list.append(revComp)
    frame_list.append(revComp[1:-2])
    frame_list.append(revComp[2:-1])

    return frame_list

print(reading_frames('CTAGCTGCA'))