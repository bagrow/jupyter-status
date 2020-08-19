# Jupyter Status
Get a quick tabular summary of running Jupyter servers and kernels.

## Usage

From the command-line, run
```
jupyter-status
```

## Example

Here I am running three jupyter lab servers on my laptop, each with a few notebooks or consoles open.

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

## Install

Install with pip:

```
pip install jupyter-status
```
