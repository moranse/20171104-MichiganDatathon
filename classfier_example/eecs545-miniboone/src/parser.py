#!/usr/bin/env python

"Parse MiniBooNE data text file and convert to numpy arrays."
import os
import sys
import argparse
import numpy as np

def main(args):
    with open(args.infile, 'r') as infile:
        # Parse the number of signal/background events
        tokens = infile.readline().split()
        num_signal_events = int(tokens[0])
        num_background_events = int(tokens[1])
    print('Parsing data...')
    data = np.genfromtxt(args.infile, skip_header=1, dtype=np.float32)
    print('Generating labels...')
    labels = np.concatenate((
        np.ones(num_signal_events, dtype=np.int8),
        np.zeros(num_background_events, dtype=np.int8)))
    print('Saving data to data.npy...')
    np.save('data', data)
    print('Saving labels to labels.npy...')
    np.save('labels', labels)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Parse MiniBooNE text file and "
            "convert to numpy arrays saved in the current directory.")
    parser.add_argument(
        'infile',
        type=str,
        help="Path to data file.")

    args = parser.parse_args()
    main(args)
