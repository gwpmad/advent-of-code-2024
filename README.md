# Advent of Code 2024

Python (and maybe C?)

## Setup

```
pip install uv # optional - only if you don't already have uv
uv venv --python 3.12
source .venv/bin/activate
uv pip install --requirements requirements.txt
```

### Setting up Ruff (VSCode)
Ruff is temperamental but:
1. Cmd+shift-P -> 'Python: Select Interpreter'
2. Use the default (`./.venv/bin/python`)
3. Click on the bottom right spinning wheel, click on Ruff
4. Allow it to select a formatter, which will likely be `black`
5. Ensure `editor.formatOnSave` is `true` in VSCode `settings.json`

## Getting solutions for a day
This will also assert that the test input specified in the day's file gave the expected response.
```
python run_day.py <day-number>
```
To run the test input assertions only, useful for avoiding long computation time:
```
python run_day.py <day-number> testonly
```
