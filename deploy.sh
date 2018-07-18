#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt
git add -f .secrets .static
git add -A
eb deploy --profile FC-8th-el --staged
git reset HEAD .secrets .static requirements.txt
rm requirements.txt
