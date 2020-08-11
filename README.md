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
python pstat.py -n/--name '<process name>' -d/--duration <duration in sec> [-i/--interval <interval in sec default 5s>]
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


##### Example Output

###### Challenge 1
```
rakesh@rakesh-NUC8i7BEH:~/PycharmProjects/temp/nexthink-task$ python3 pstat.py -n 'Xorg' -d 10
Xorg [pid: 1774]: average [cpu_usage: 0.0, private_memory: 397402112.0, open_files: 1.0]: memory_usage_increasing: False
Xorg [pid: 1774]: average [cpu_usage: 0.0, private_memory: 397412352.0, open_files: 1.0]: memory_usage_increasing: True
```

```
rakesh@rakesh-NUC8i7BEH:~/PycharmProjects/temp/nexthink-task$ cat Xorg_1774.csv 
cpu_usage,private_memory,open_files
0.0,397402112,1
0.0,397422592,1
```

###### Challenge 2
```
rakesh@rakesh-NUC8i7BEH:~/PycharmProjects/temp/nexthink-task$ python3 test_pstat.py 
..java [pid: 5979]: average [cpu_usage: 1.98, private_memory: 726802432.0, open_files: 321.0]: memory_usage_increasing: False
java [pid: 5979]: average [cpu_usage: 0.99, private_memory: 726802432.0, open_files: 321.0]: memory_usage_increasing: True
...usage: pstat [-h] -n NAME -d DURATION [-i INTERVAL]
pstat: error: the following arguments are required: -n/--name
.usage: pstat [-h] -n NAME -d DURATION [-i INTERVAL]
pstat: error: the following arguments are required: -d/--duration
.java [pid: 5979]: average [cpu_usage: 0.0, private_memory: 726802432.0, open_files: 321.0]: memory_usage_increasing: False
java [pid: 5979]: average [cpu_usage: 1.0, private_memory: 726802432.0, open_files: 321.0]: memory_usage_increasing: True
.java [pid: 5979]: average [cpu_usage: 0.0, private_memory: 726802432.0, open_files: 321.0]: memory_usage_increasing: False
.
----------------------------------------------------------------------
Ran 9 tests in 11.834s

OK
```

