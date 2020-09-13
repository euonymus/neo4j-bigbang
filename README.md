# Neo4j Big Bang the CSV importer for Neo4j
This is a python shell to import csv data into neo4j database.
You can import both Nodes and Relationships.
You don't need to write any Cypher script at all.

# What it can do

## Importing Nodes
- This shell automatically detects the types of properties.
- You can choose skipping or updating if nodes already exist.
- You can choose Node labels row by row. Multiple labels are supported.
- You can set labels as your importing file name too.

## Importing Relationships
- This shell automatically detects the types of properties.
- You can choose skipping or updating if relationship already exists.
- You can choose if you want to create nodes at the same time.
- You can choose Relationship type row by row.
- You can set type as your importing file name too.


# Prepare CSV Data

Put your importing CSV file under `importing` directory


# Getting Started

```bash
$ cd [path to this repo]
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

# Import Nodes from CSV

Run

```bash
$ python neo4j_big_bang/import_nodes.py

# Case 1: Use Labels from file name Person|Employee.csv
$ python neo4j_big_bang/import_nodes.py -n Person|Employee.csv -f

# Case 2: Update if target node already exists
$ python neo4j_big_bang/import_nodes.py -n Person|Employee.csv -f -l Person|Teacher -p name|employee_id -u

# Case 3: Skip if target node already exists
$ python neo4j_big_bang/import_nodes.py -n Person|Employee.csv -f -l Person|Teacher -p name|employee_id
```

Options

- `-u` : If set, update node when it exists. ( both -l and -p are required )
- `-n` : Specify CSV file name. Its' required when you set `-f`
- `-f` : Set if you want to use file name as labels. If not set, labels field is required in the CSV file
- `-l` : Unique Labels. Its' required when you set `-u`
- `-p` : Unique Properties. Its' required when you set `-u`


# Import Relationships from CSV

Run

```bash
$ python neo4j_big_bang/import_relationships.py

# Case 1: Use Type from file name YOUR_RELATION_TYPE.csv
$ python neo4j_big_bang/import_relationships.py -n YOUR_RELATION_TYPE.csv -f

# Case 2: Update if same type relationship already exists
$ python neo4j_big_bang/import_relationships.py -u

# Case 3: Create relationship and nodes at once, even though nodes does not exist
$ python neo4j_big_bang/import_relationships.py -c
```

Options

- `-u` : If set, update relationship when it exists
- `-n` : Specify CSV file name. Its' required when you set `-f`
- `-f` : Set if you want to use file name as relationship type. If not set, type field is required in the CSV file
- `-c` : If you want to create nodes at the same time, use this option

