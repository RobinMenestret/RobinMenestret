import os
from shutil import copyfile,copytree

TEST_DATA_PATH = 'test'+os.sep+'test_data'+os.sep
TEST_GENERATED_ARIFACTS_PATH= 'test'+os.sep+'generated_artifacts'+os.sep

MAQUETTE_JSON_FILE_NAME="maquette.json"
MAQUETTE_PRELIM_ALLOCATION_FILE_NAME="maquette_prelim_alloc-distributed.xlsx"
MAQUETTE_SINGLE_RACK_PRELIM_ALLOCATION_FILE_NAME="maquette_prelim_alloc-rack1.xlsx"
EXPORTED_RACK_ALLOCATION_FILE_NAME="rack_allocations_for_maquette.xlsx"
ALLOCATION_PARAMETER_FILE="hallo-parameters.yaml"

SIMFD_WORKSPACE="simfd-workspace"
def create_generated_artifacts_folder():
    clean_directory()
    os.mkdir(TEST_GENERATED_ARIFACTS_PATH)

def clean_directory(dir=TEST_GENERATED_ARIFACTS_PATH):
    if os.path.exists(dir):
        for element in os.listdir(dir):
            if os.path.isdir(dir+element):
                clean_directory(dir+element+os.sep)
            if os.path.isfile(dir+element):
                os.remove(dir+element)
        os.rmdir(dir)

def copy_test_data_file_in_generated_artifacts(data_file_name):
    copyfile(TEST_DATA_PATH+data_file_name,TEST_GENERATED_ARIFACTS_PATH+data_file_name)

def copy_test_data_folder_in_generated_artifacts(folder_name):
    copytree(TEST_DATA_PATH+folder_name,TEST_GENERATED_ARIFACTS_PATH+folder_name)