#### nexthink-task
Software Engineering Quiz

##### Dependencies
```
Python: v3.8.2
```
To install dependencies,
```
pip install requirements.txt
```

##### Run

###### Challenge 1
```
usage: pstat [-h] -n NAME -d DURATION [-i INTERVAL]
pstat: error: the following arguments are required: -n/--name, -d/--duration
```
e.g.
`python pstat.py -n 'chrome' --duration 60 --interval 5`

* Metrics will be saved in file with name syntax: `<process_name>_<pid>.csv`.
* Multiple files are created if sub-processes are associated with process.


###### Challenge 2
`python test_pstat.py`

* Syntax and critical functional tests are implemented


###### Platform Independence
* Not verified on Windows and MacOS
* According to specification of [psutil](https://psutil.readthedocs.io/en/latest/), methods used in program are supported on Linux, Windows and MacOS


