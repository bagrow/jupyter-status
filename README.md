# Jupyter Status
Get a quick tabular summary of running Jupyter servers and kernels. Especially useful as a status board when embedded in your desktop using [GeekTool](https://www.tynsoe.org/v2/geektool/), [Ubersicht](http://tracesof.net/uebersicht/), [Conky](https://github.com/brndnmtthws/conky), or the like.


## Example

Here I have three jupyter lab servers running on my machine, each with a few notebooks or consoles open:

```
localhost:8888 /Users/bagrow/projects/research-project-01/notebooks
Name                                   Type      Kernel               Last active       Status
-------------------------------------  --------  -------------------  ----------------  --------
Console 1                              console   research-project-01  2020-08-19 22:28  idle
Console 2                              console   research-project-01  2020-08-19 22:28  idle
Console 3                              console   research-project-01  2020-08-19 22:28  idle
01-jpb-explore-data.ipynb              notebook  research-project-01  2020-08-19 22:28  idle
jpb-log_2020-08-19.ipynb               notebook  research-project-01  2020-08-19 22:28  idle

localhost:8889 /Users/bagrow/projects/cool-science-playground/notebooks
Name                                   Type      Kernel                     Last active       Status
-------------------------------------  --------  -------------------------  ----------------  --------
Console 1                              console   cool-science-playground    2020-08-19 22:28  idle

localhost:8890 /Users/bagrow/projects/research-project-02/notebooks
Name                             Type      Kernel               Last active       Status
-------------------------------  --------  -------------------  ----------------  --------
Console 1                        console   research-project-02  2020-08-16 16:17  idle
01.0-jpb-explore-data.ipynb      notebook  research-project-02  2020-08-16 16:18  idle
02.0-jpb-big-simulation.ipynb    notebook  research-project-02  2020-08-19 22:28  running
jpb-log_2020-08-15.ipynb         notebook  research-project-02  2020-08-16 16:17  idle
```

I find kernel names are helpful when using [per-project environments](https://dev.to/rgalbo/simple-python-environments-for-data-science--4pha) (in my case, with [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)).

## Usage

From the command-line, run:
```
jupyter-status
```
Or if you want an html table:
```
jupyter-status html
```

Arguments to `jupyter-status` are passed to [tabulate's `tablefmt` option](https://github.com/astanin/python-tabulate#table-format).

## Install

Install with pip:

```
pip install jupyter-status
```
