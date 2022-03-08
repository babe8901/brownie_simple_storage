from msilib.schema import Directory
from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # print(SimpleStorage[0])

    # Brownie already knows the ABI from the contracts directory
    print(simple_storage.retrieve())


def main():
    read_contract()
