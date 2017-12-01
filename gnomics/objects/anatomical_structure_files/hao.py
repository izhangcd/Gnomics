#
#
#
#
#

#
#   IMPORT SOURCES:
#


#
#   HAO ID.
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

#   Other imports.
import json
import requests

#   MAIN
def main():
    hao_unit_tests()
    
# Return HAO ID.
def get_hao_id(anat):
    hao_array = []
    for ident in anat.identifiers:
        if ident["identifier_type"].lower() == "hao id" or ident["identifier_type"].lower() == "hao identifier":
            hao_array.append(ident["identifier"])
    return hao_array
    
#   UNIT TESTS
def hao_unit_tests():
    print("NOT FUNCTIONAL.")
    
#   MAIN
if __name__ == "__main__": main()