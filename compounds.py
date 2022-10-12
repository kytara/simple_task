#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jakub Svoboda, <jakub.svoboda.cs@outlook.com>
"""

import requests

def norm(org_name):
    """
    For a common compound name, find its normalized variant.
    Source API: PubChem

    Parameters
    ----------
    org_name : str
        Compound name.

    Returns
    -------
    norm_name : str
        Normalized compound name.

    """
    # Get list of synonyms from PubChem
    response = requests.get(
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{org_name}/synonyms/JSON"
    ).json()
    # First synonym ~ normalized form
    normed_form = response["InformationList"]["Information"][0]["Synonym"][0].upper()
    return normed_form
