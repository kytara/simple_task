This Docker image takes a list of compound names (hardcoded in main.py),
and prints a nicely formatted table of their corresponding normalized names.

I used the PubChem PUG REST API to fetch the list of synonyms. I am assuming
the first synonym is equivalent to the normalized compound name.

I've put in a 1 second sleep every 5 requests as to (trivially) comply with 
the PubChem PUG API's rule not to send more than 5 requests per second.

Intended use:
```bash
docker build -t norm_compounds .
docker run norm_compounds
```
