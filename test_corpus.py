#!/usr/bin/env python -*- coding: utf-8 -*-


from pywsd.semcor import SemCorpus

semcor = SemCorpus('pywsd/data/semcor3.0_naf')

for filename, sentence in semcor:
    context_sent_str = [i.text for i in sentence]
    context_sent_pos = [i.term.pos for i in sentence]
    
    print context_sent_str
    print context_sent_pos
    print


######################################################################


from pywsd.semeval import SemEval2007_Coarse_WSD

semeval = SemEval2007_Coarse_WSD('pywsd/data/semeval2007_coarse_grain_wsd/')

for i in semeval:
    print i