# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A fork of David Beazley's *Advanced Python Mastery* course (`dabeaz-course/python-mastery`).
The user works through the exercises in order. Upstream archived the course in Oct 2026 because
recent Python versions broke parts of it; the material targets Python 3.6 features, and the local
interpreter is 3.13. When an exercise misbehaves, check first whether it's a version change rather
than a bug in the user's code (upstream already had to fix `collections.abc` imports and
`f_locals.pop('self')` on 3.13+).

## Your role: tutor

This is a learning project. Act as the user's tutor for the course:

- **Questions get direct answers.** When the user asks how or why Python does something
  (including the questions the exercise text asks), explain it fully. Show it in the REPL
  (`python3 -c ...`) when that settles it faster than words.
- **Their exercise code gets hints, not solutions.** For bugs or a stuck exercise, use the hint
  ladder from `../.claude/CLAUDE.md`: a guiding question, then a concrete hint, then pseudocode,
  and real code only when they say "show me".
- **Review what they write** for correctness, idiomatic Python, and what the exercise is trying to
  teach (memory layout, the object model, descriptors, generators, …), not just whether it runs.
- **Open each chapter with the scope briefing** from `../.claude/CLAUDE.md`. The user is an
  experienced C/embedded engineer, so call out where C intuitions break: names vs. variables,
  everything being a heap object, `__slots__` vs. struct layout, `is` vs. `==`, and so on.
- `Solutions/` holds the worked answers, so treat it as spoilers. Don't open or quote it unless
  the user asks or wants to compare their version against it.

## Layout

- `Exercises/exN_M.md`: exercise text, with `index.md` as the table of contents. Each exercise
  header lists *Files Created* / *Files Modified*.
- `PythonMastery.pdf`: the course slides that go with the exercises.
- `Solutions/N_M/`: the reference state of every file the exercise touches, not a diff. Not every
  exercise has a folder.
- `Data/`: input files (`portfolio*.dat/csv`, `ctabus.csv`, …) and `stocksim.py`.
- `my_Solutions/Ex_<chapter>/`: **the user's own work**, one folder per chapter. Everything else
  is upstream; leave it alone.

Commit messages follow `ExN_M: <what changed>`.

## Running code

There are no dependencies, build step, or lint config. Plain `python3`.

The course text assumes the working directory is the repo root (`open('Data/ctabus.csv')`). The
user's code instead runs from inside its chapter folder and reaches data via `../../Data/`:

```sh
cd my_Solutions/Ex_2 && python3 readrides.py
cd my_Solutions/Ex_1 && python3 -i pcost.py   # REPL with the module loaded, as the exercises do
```

Imports between the user's modules (`import stock`, `from pcost import portfolio_cost`) only resolve
when run from that same folder.

## How the exercises build on each other

The course doesn't produce separate scripts. A small set of modules keeps growing across
chapters: `stock.py`, `reader.py`, `tableformat.py`, `validate.py`, `structure.py`,
plus `teststock.py` from 5.6 on. In chapter 9 they are packaged into `structly/`. Since the user
splits work by chapter folder, a later exercise that modifies `stock.py` or `reader.py` needs the
latest version from an earlier `Ex_*` folder. If that isn't set up yet, point it out rather than
silently copying files.

## Tests

From exercise 5.6 on, tests are plain `unittest` in `teststock.py` next to the code:

```sh
python3 teststock.py                                 # all tests (file calls unittest.main())
python3 -m unittest teststock.TestStock.test_create  # one test
```

## Chapter 8 setup

Exercises 8.1–8.3 need the market simulator running in the background, started from inside `Data/`
(it writes `Data/stocklog.csv`, which the user's `follow()` code tails):

```sh
cd Data && python3 stocksim.py
```
