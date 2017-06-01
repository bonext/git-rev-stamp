#!/usr/bin/env bash

# prepare post-commit hook
git rev-parse HEAD > ../.HEAD_COMMIT
ln -s ../../hash-stamp/post-commit ../.git/hooks/post-commit

# filters
git config --local filter.tsrev.clean "hash-stamp/tsrev.py --clean"
git config --local filter.tsrev.smudge "hash-stamp/tsrev.py"
