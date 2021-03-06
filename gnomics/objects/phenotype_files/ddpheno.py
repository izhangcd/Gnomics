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
#   Convert to Dictyostelium Discoideum Phenotype Ontology (DDPHENO).
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
import gnomics.objects.phenotype

#   Other imports.
import json
import requests
import time

#   MAIN
def main():
    ddpheno_unit_tests()

#   Get DDPHENO ID.
def get_ddpheno_id(phen, user=None):
    ddpheno_id_array = []
    for ident in phen.identifiers:
        if ident["identifier_type"].lower() in ["ddpheno", "ddpheno id", "ddpheno identifier"]:
            if ident["identifier"] not in ddpheno_id_array:
                ddpheno_id_array.append(ident["identifier"]) 
    return ddpheno_id_array
        
#   UNIT TESTS
def ddpheno_unit_tests():
    print("NOT FUNCTIONAL.")

#   MAIN
if __name__ == "__main__": main()