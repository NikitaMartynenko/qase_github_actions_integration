name: Docker Image CI

on:
#  push:
#    branches: [ "main" ]
  workflow_dispatch:
    branches: [ "main" ]

jobs:
  build:
    strategy:
      matrix:
        python-version: ["3.10"]
    name: "Python ${{ matrix.python-version }}"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r qase_github_actions_integration/requirements.txt
      - name: Run unit tests
        run: cd qase_github_actions_integration/tests && pytest .

