# Neo4j Big Bang the CSV importer for Neo4j
This is a python package to import csv data into neo4j database.
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


# Getting Started

## Install this package

```
$ pip install neo4j-bigbang
```

## Prepare CSV Data

Put your importing CSV file under `importing` directory

## Run command with environment variables

```
NEO4J_URI=bolt://localhost:7687 NEO4J_USER=neo4j NEO4J_PASSWORD={your-password} bigbang-node
```

## Or set envilonment variable
```
export NEO4J_URI=bolt://localhost:7687 NEO4J_USER=neo4j NEO4J_PASSWORD=password
```


# Getting Started from source

```bash
$ cd [path to this repo]
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

Setup your .env file under `src/bigbang` directory


/src/bigbang/.env
```
NEO4J_URI='bolt://localhost:7687'
NEO4J_USER='neo4j'
NEO4J_PASSWORD='password'
```

# Import Nodes from CSV

Run

```bash
$ python src/bigbang/import_nodes.py

# Case 1: Use Labels from file name Person|Employee.csv
$ python src/bigbang/import_nodes.py -n Person|Employee.csv -a

# Case 2: Update if target node already exists
$ python src/bigbang/import_nodes.py -n Person|Employee.csv -a -l Person|Teacher -p name|employee_id -u

# Case 2': Update if target node already exists ( labels should be on CSV )
$ python src/bigbang/import_nodes.py -n Person|Employee.csv -a -p name|employee_id -u

# Case 3: Skip if target node already exists
$ python src/bigbang/import_nodes.py -n Person|Employee.csv -a -l Person|Teacher -p name|employee_id

# Case 3': Skip if target node already exists ( labels should be on CSV )
$ python src/bigbang/import_nodes.py -n Person|Employee.csv -a -l -p name|employee_id
```

Options

- `-p` with `specified properties`: Unique Properties. If not set, target property will be 'neme'.
- `-l` with `specified labels` : If set, specified labels will be targeted if already in Neo4j.
- `-n` : Specify CSV file name. Its' required when you set `-f`
- `-a` : Set if you want to use file name as labels. If not set, labels field is required in the CSV file
- `-f` : Force inserting node. -p and -l -u are ignored.
- `-u` : If set, update node when it exists. ( both -l and -p are required )


# Import Relationships from CSV

Run

```bash
$ python src/bigbang/import_relationships.py

# Case 1: Use Type from file name YOUR_RELATION_TYPE.csv
$ python src/bigbang/import_relationships.py -n YOUR_RELATION_TYPE.csv -a

# Case 2: Update if same type relationship already exists
$ python src/bigbang/import_relationships.py -u

# Case 3: Create relationship and nodes at once, even though nodes does not exist
$ python src/bigbang/import_relationships.py -c
```

Options

- `-u` : If set, update relationship when it exists
- `-n` : Specify CSV file name. Its' required when you set `-a`
- `-a` : Set if you want to use file name as relationship type. If not set, type field is required in the CSV file
- `-c` : If you want to create nodes at the same time, use this option

