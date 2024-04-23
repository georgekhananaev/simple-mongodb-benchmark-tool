# Simple MongoDB Benchmark Tool

The Simple MongoDB Benchmark Tool is a Python-based utility designed to measure and analyze the performance of MongoDB operations across a variety of scenarios. It assesses the execution speed for traditional CRUD operations as well as bulk inserts and complex queries, providing clear visual indications of progress and detailed metrics for each type of operation.

## Screenshot

![alt text](https://github.com/georgekhananaev/simple-mongodb-benchmark-tool/blob/main/screenshot.png?raw=true)

## Background

MongoDB, a powerful NoSQL database, is widely used in various applications due to its high performance, high availability, and easy scalability. Understanding its performance characteristics under different workloads is crucial for optimizing interactions and infrastructure decisions. This tool aims to provide developers and database administrators with a comprehensive means to benchmark MongoDB operations and gain insights into potential optimizations.

## Features

- **Simple Command-Line Interface**: Easy to execute with comprehensive options.
- **Progress Indicators**: Utilizes `tqdm` for real-time progress updates.
- **Detailed Metrics**: Time measurements help identify bottlenecks in database operations.
- **Extended Testing Capabilities**: Includes bulk inserts, complex query testing, and concurrency testing to simulate more realistic application scenarios.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- MongoDB running on your local machine or remotely accessible

### Setup

1. **Clone the repository** (or download the zip file and extract it)

   ```bash
   git clone https://github.com/georgekhananaev/simple-mongodb-benchmark-tool.git
   cd simple-mongodb-benchmark-tool
	```
 
2. **Setup a virtual environment** (Recommended)
  
	```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
 
3. **Install required packages**

    ```bash
    pip install -r requirements.txt
    ```
   

### Usage
Run the tool from the command line with various parameters to control the number and type of operations:

```bash
python mongodb_benchmark.py --inserts 1000 --reads 1000 --updates 1000 --deletes 1000 --bulk-inserts 5000 --complex-queries 100 --concurrency 4
```
  
**Detailed Usage**
```
--host: Specify the MongoDB host. Default is localhost.
--port: Specify the MongoDB port. Default is 27017.
--db: Specify the database name. Default is benchmark.
--inserts: Number of documents to insert.
--reads: Number of documents to read.
--updates: Number of documents to update.
--deletes: Number of documents to delete.
--bulk-inserts: Number of documents for bulk insert operations.
--complex-queries: Number of complex queries to perform.
--concurrency: Level of concurrency for operations.
```

**Example**
To run a benchmark with varied operations on a database named testdb with custom port:
```bash
python mongodb_benchmark.py --host localhost --port 27117 --db testdb --inserts 500 --reads 1500 --updates 1000 --deletes 300 --bulk-inserts 2000 --complex-queries 100 --concurrency 4
```

### License
Distributed under the MIT License. See LICENSE for more information.


### Author
George Khananaev
