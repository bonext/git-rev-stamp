#!/usr/bin/env bash
cwd=${PWD##*/}

# prepare post-commit hook
git rev-parse HEAD > ../.HEAD_COMMIT
ln -s $cwd/post-commit ../.git/hooks/post-commit

# filters
git config --local filter.tsrev.clean "$cwd/tsrev.py --clean"
git config --local filter.tsrev.smudge "$cwd/tsrev.py"
