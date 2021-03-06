#!/usr/bin/env python

#
#
#
#
#

#
#   IMPORT SOURCES:
#
#

#
#   Get SNOMED.
#

#   PRE-CODE
import faulthandler
faulthandler.enable()

#   IMPORTS

#   Imports for recognizing modules.
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

#   Import modules.
from gnomics.objects.user import User
import gnomics.objects.anatomical_structure
import gnomics.objects.auxiliary_files.identifier

#   Other imports.
import json
import requests
import timeit

#   MAIN
def main():
    snomed_unit_tests("21", "50801", "c8ec0cca-e10f-485b-bf82-ea0e07000f4f")

# Return SNOMED.
def get_snomed(anat, user=None, source="umls"):
    anat_array = []
    
    for iden in anat.identifiers:
        if iden["identifier_type"].lower() in ["neu id", "neu identifier"]:
    
            if source.lower() in ["umls", "all"]:
                anat_array = []

                umls_tgt = User.umls_tgt(user)
                page_num = 0
                base = "https://uts-ws.nlm.nih.gov/rest"
                ext = "/crosswalk/current/source/NEU/" + iden["identifier"]

                while True:
                    tick = User.umls_st(umls_tgt)
                    page_num += 1
                    query = {"ticket": tick, "pageNumber": page_num}
                    r = requests.get(base+ext, params=query)
                    r.encoding = 'utf-8'
                    items = json.loads(r.text)
                    json_data = items["result"]
                    for rep in json_data:
                        if rep["ui"] not in anat_array and rep["ui"] != "NONE":

                            # SNOMED 1982.
                            if rep["rootSource"] == "SNM":
                                anat_array.append(rep["ui"])
                                gnomics.objects.anatomical_structure.AnatomicalStructure.add_identifier(anat, identifier=rep["ui"], identifier_type="SNOMED 1982", language=None, source="UMLS Metathesaurus")
                            
                            # SNOMED International 1998
                            elif rep["rootSource"] == "SNMI":
                                anat_array.append(rep["ui"])
                                gnomics.objects.anatomical_structure.AnatomicalStructure.add_identifier(anat, identifier=rep["ui"], identifier_type="SNOMED International 1998", language=None, source="UMLS Metathesaurus")

                    if not json_data:
                        break
            
        elif iden["identifier_type"].lower() == "uwda id" or iden["identifier_type"].lower() == "uwda identifier":
    
            if source.lower() in ["umls", "all"]:

                umls_tgt = User.umls_tgt(user)
                page_num = 0
                base = "https://uts-ws.nlm.nih.gov/rest"
                ext = "/crosswalk/current/source/UWDA/" + iden["identifier"]

                while True:
                    tick = User.umls_st(umls_tgt)
                    page_num += 1
                    query = {"ticket": tick, "pageNumber": page_num}
                    r = requests.get(base+ext, params=query)
                    r.encoding = 'utf-8'
                    items = json.loads(r.text)
                    json_data = items["result"]
                    for rep in json_data:
                        if rep["ui"] not in anat_array and rep["ui"] != "NONE":

                            # SNOMED 1982.
                            if rep["rootSource"] == "SNM":
                                anat_array.append(rep["ui"])
                                gnomics.objects.anatomical_structure.AnatomicalStructure.add_identifier(anat, identifier=rep["ui"], identifier_type="SNOMED 1982", language=None, source="UMLS Metathesaurus")
                            
                            # SNOMED International 1998
                            elif rep["rootSource"] == "SNMI":
                                anat_array.append(rep["ui"])
                                gnomics.objects.anatomical_structure.AnatomicalStructure.add_identifier(anat, identifier=rep["ui"], identifier_type="SNOMED International 1998", language=None, source="UMLS Metathesaurus")

                    if not json_data:
                        break

    return anat_array
    
#   UNIT TESTS
def snomed_unit_tests(neu_id, uwda_id, umls_api_key):
    user = User(umls_api_key = umls_api_key)
            
    neu_anat = gnomics.objects.anatomical_structure.AnatomicalStructure(identifier = neu_id, identifier_type = "NEU ID", source = "UMLS")
    print("Getting SNOMED identifiers from NEU ID (%s):" % neu_id)
    for snomed in get_snomed(neu_anat, user = user):
        print("- " + str(snomed))
        
    uwda_anat = gnomics.objects.anatomical_structure.AnatomicalStructure(identifier = uwda_id, identifier_type = "UWDA ID", source = "UMLS")
    print("\nGetting SNOMED identifiers from UWDA ID (%s):" % uwda_id)
    for snomed in get_snomed(uwda_anat, user = user):
        print("- " + str(snomed))
    
#   MAIN
if __name__ == "__main__": main()