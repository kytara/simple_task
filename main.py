#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jakub Svoboda, <jakub.svoboda.cs@outlook.com>
"""

import time
import pandas as pd
import compounds

if __name__ == "__main__":
    org_names = ["Adenosine","Adenocard","BG8967","Bivalirudin",
                 "BAYT006267","diflucan","ibrutinib","PC-32765"]
    normed_form = [""] * len(org_names)
    
    for i in range(len(org_names)):
        normed_form[i] = compounds.norm(org_names[i])

        # To naively comply with PubChem PUG REST's 
        # "less than 5 requests / second" rule
        if i % 5 == 0:
            time.sleep(1)
    
    norm_table = pd.DataFrame({"org_name": org_names, "normed_form": normed_form})
    print(norm_table)
        