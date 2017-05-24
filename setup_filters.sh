#!/usr/bin/env bash

# prepare post-commit hook
git rev-parse HEAD > .HEAD_COMMIT
ln -s ../../.git-machinery/post-commit .git/hooks/post-commit

# filters
git config --local filter.tsrev.clean ".git-machinery/tsrev.py --clean"
git config --local filter.tsrev.smudge ".git-machinery/tsrev.py"
