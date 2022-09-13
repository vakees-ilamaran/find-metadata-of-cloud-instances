#!/usr/bin/env python3

"""
Description:
    Get the Metadata from aws instance
Abstract: 
    This uses the request module to get all the metadata structure.
    Using recursive model it gets the output of all the directory and populate the result
Author: 
    vakees.ilamaran@gmail.com
"""

import requests
import json
import argparse
import sys

class FindMetadata():
    def __init__(self, key_to_find) -> None:
        self.key_to_find = key_to_find
        self.metadata_url = "http://169.254.169.254/latest/"
        self.metadata_data = self.get_metadata_from_endpoint()
        if self.metadata_data is not None:
            print("Metadata is retrived")
            print(self.metadata_data)
        else:
            print("Unable to find the metadata")
            sys.exit(1)
        if self.key_to_find != "NNNN":
            print("A Key is specified hence finding the key")
            temp = self.gen_dict_extract(self.key_to_find, self.metadata_data)
            print(temp)
            
    def get_metadata_from_endpoint(self) -> dict:
        metadata_retrived = self.get_from_tree(self.metadata_url, ["meta-data/"])
        return metadata_retrived
    
    def get_from_tree(self, url_new, tree_path) -> dict:
        result = {}
        for each_item in tree_path:
            r = requests.get(url_new + each_item)
            text = r.text
            if each_item[-1] == "/":
                list_of_values = r.text.splitlines()
                result[each_item[:-1]] = self.get_from_tree(url_new, list_of_values)
            elif self.is_json(text):
                result[each_item] = json.loads(text)
            else:
                result[each_item] = text
        return result

    def is_json(self, myjson) -> bool:
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True 

    def gen_dict_extract(self, key, var):
        if hasattr(var, 'items'):
            for k, v in var.items():
                if k == key:
                    yield v
                if isinstance(v, dict):
                    for result in self.gen_dict_extract(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in self.gen_dict_extract(key, d):
                            yield result

def parsing_args():
    """
    We get the command line arguments and parse it to use it !!
    :return: returns the parse object
    """

    parser = argparse.ArgumentParser(
        prog='finding-Metadata',
        epilog='Enjoy the CLI Team!' )

    parser.add_argument(
        '--find_key', 
        metavar ='key_to_find', 
        type = str,
        default="NNNN",
        required = False,
        help = 'The key to find in the metadata api')

    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s V1.0.0')   
    
    return parser.parse_args()


def main():
    try:
        args = parsing_args()
        kpmg_dummy_object = FindMetadata(args.key_to_find)

    except Exception as e:
        print("There is some issue with the main function")
        print("Please contact the GitHub Contributor for troubleshooting")
        sys.exit(e)

if __name__ == "__main__":
    main()