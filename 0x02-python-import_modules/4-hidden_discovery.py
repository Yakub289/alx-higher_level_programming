#!/usr/bin/python3

import hidden_4

def principal():
    for sequences in dir(hidden_4):
        if not (sequences[0] == '_' and sequences[1] == '_'):
            print(sequences)
            if __name__ == "__main__":
                principal()
