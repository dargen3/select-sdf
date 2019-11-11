#!/usr/bin/env python3
import argparse
from collections import Counter

def load_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_sdf", help="Sdf file with molecules.")
    parser.add_argument("--output_sdf", help="File to store sdf with selected molecules.")
    parser.add_argument("--atomic_types", help="Atomic types defining selected molecules.")
    args = parser.parse_args()
    if args.input_sdf is None or args.output_sdf is None or args.atomic_types is None:
            parser.error("ERROR! --input_sdf, --output_sdf and --atomic_types arguments are required")
    return args


if __name__ == '__main__':
    args = load_arguments()
    atomic_types = set(args.atomic_types.split(","))

    #counter = Counter()

    new_sdf_string = ""
    for molecule_data in [x.splitlines() for x in open(args.input_sdf, "r").read().split("$$$$\n")][:-1]:
        molecule_atomic_symbols = set([atom_line.split()[3] for atom_line in molecule_data[4: int(molecule_data[3][:3]) + 4]])
        #counter.update(molecule_atomic_symbols)
        if molecule_atomic_symbols.issubset(atomic_types):
            new_sdf_string += "\n".join(molecule_data) + "$$$$\n"


    with open(args.output_sdf, "w") as output_sdf:
        output_sdf.write(new_sdf_string)

    #from pprint import pprint ; pprint(counter.most_common())