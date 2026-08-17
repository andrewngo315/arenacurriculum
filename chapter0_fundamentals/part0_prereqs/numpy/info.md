# NumPy — 100 exercises

ARENA's prerequisites page asks for NumPy alongside the Python material:

> Working through [these 100 basic NumPy exercises](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb)
> would be a good idea, or if you're comfortable with NumPy already then you could try
> doing them in PyTorch.

`100_Numpy_exercises.ipynb` is that notebook, from
[rougier/numpy-100](https://github.com/rougier/numpy-100) (MIT, see `LICENSE.txt`).
Each question is a markdown cell followed by an empty code cell. Difficulty runs
★☆☆ to ★★★.

The upstream notebook opens with `%run initialise.py`, which enables `hint(n)` and
`answer(n)` lookups inline. That cell is removed here. Same reason the Python drills
have no worked solutions in them: I write the answer first, then mark against
`100_Numpy_exercises_with_solutions.md`, then have the mark audited. A hint I can
reach mid-question is a hint I will reach for.

The solutions and hints files are kept locally and gitignored — they are the answer
key, not my work.

Run the notebook on the project venv (`.venv`, Python 3.11), not system Python.
