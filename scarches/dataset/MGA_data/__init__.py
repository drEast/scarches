try:
    from .MGA_data import seqFISH1_1, seqFISH2_1, seqFISH3_1, seqFISH1_2, seqFISH2_2, seqFISH3_2, scRNAseq
except:
    import warnings
    warnings.warn('In order to use the mouse gastrulation seqFISH datsets, please install squidpy (see https://github.com/scverse/squidpy).')
