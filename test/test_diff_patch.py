# test_diff_patch.py
# David Prager Branner
# 20140609

import os
import diff_patch as P

# Set up
directory = 'example'
from_file = 'test_from.txt'

def test_patch_01():
    to_file = 'test_to_01.txt'
    diff_file = 'diff_01.txt'
    P.diff(directory, from_file, to_file, diff_file)
    patched_file = P.patch(directory, diff_file, from_file)
    with open(os.path.join(directory, to_file), 'r') as f:
        to_contents = f.read()
    to_contents = to_contents.split('\n')
    assert patched_file == to_contents

def test_patch_02():
    to_file = 'test_to_02.txt'
    diff_file = 'diff_02.txt'
    P.diff(directory, from_file, to_file, diff_file)
    patched_file = P.patch(directory, diff_file, from_file)
    with open(os.path.join(directory, to_file), 'r') as f:
        to_contents = f.read()
    to_contents = to_contents.split('\n')
    assert patched_file == to_contents

def test_patch_03():
    to_file = 'test_to_03.txt'
    diff_file = 'diff_03.txt'
    P.diff(directory, from_file, to_file, diff_file)
    patched_file = P.patch(directory, diff_file, from_file)
    with open(os.path.join(directory, to_file), 'r') as f:
        to_contents = f.read()
    to_contents = to_contents.split('\n')
    assert patched_file == to_contents

def test_patch_04():
    to_file = 'test_to_04.txt'
    diff_file = 'diff_04.txt'
    P.diff(directory, from_file, to_file, diff_file)
    patched_file = P.patch(directory, diff_file, from_file)
    with open(os.path.join(directory, to_file), 'r') as f:
        to_contents = f.read()
    to_contents = to_contents.split('\n')
    assert patched_file == to_contents

#def test_patch_99():
#    from_file = 'first.txt'
#    to_file = 'second.txt'
#    diff_file = 'diff.txt'
#    P.diff(directory, from_file, to_file, diff_file)
#    patched_file = P.patch(directory, diff_file, from_file)
#    with open(os.path.join(directory, to_file), 'r') as f:
#        to_contents = f.read()
#    to_contents = to_contents.split('\n')
#    assert patched_file == to_contents
