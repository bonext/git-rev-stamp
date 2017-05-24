#!/usr/bin/env python
#  vim: set fileencoding=utf-8 :
import sys
import re
import argparse
import datetime

COMMIT_INFO_FILE = '.HEAD_COMMIT'

smudge_re = re.compile(r'\$tsrev\$')
smudge_p = '$tsrev: %s $'

clean_re = re.compile(r'\$tsrev.+\$')
clean_p = '$tsrev$'

def tsrev(rev="xxx"):
    now = datetime.datetime.now()
    return '%s -- rev. %s' % (now.strftime('%Y-%m-%d %H:%M'), rev)


def clean():
    for line in sys.stdin.readlines():
        line = clean_re.sub(clean_p, line)
        sys.stdout.write(line)


def smudge():
    with open(COMMIT_INFO_FILE, 'r') as f:
        rev = f.read().strip()
    for line in sys.stdin.readlines():
        line = smudge_re.sub(smudge_p % tsrev(rev), line)
        sys.stdout.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args()
    if args.clean:
        clean()
    else:
        smudge()

