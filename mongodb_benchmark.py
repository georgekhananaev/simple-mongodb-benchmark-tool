import argparse
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from tqdm import tqdm
from threading import Thread


def connect_to_mongo(host, port, db_name):
    """ Establish a connection to MongoDB. """
    try:
        client = MongoClient(host, port)
        db = client[db_name]
        print(f"Connected to MongoDB at {host}:{port}")
        return db
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None


def perform_inserts(db, num_inserts):
    """ Perform insert operations. """
    collection = db['test_data']
    start_time = time.time()
    for i in tqdm(range(num_inserts), desc="Inserting Documents"):
        document = {'index': i, 'timestamp': time.time()}
        collection.insert_one(document)
    elapsed = time.time() - start_time
    print(f"Inserted {num_inserts} documents in {elapsed: .2f} seconds.")


def perform_reads(db, num_reads):
    """ Perform read operations. """
    collection = db['test_data']
    start_time = time.time()
    for _ in tqdm(range(num_reads), desc="Reading Documents"):
        cursor = collection.find()
        _ = list(cursor)
    elapsed = time.time() - start_time
    print(f"Performed {num_reads} read operations in {elapsed: .2f} seconds.")


def perform_updates(db, num_updates):
    """ Perform update operations. """
    collection = db['test_data']
    start_time = time.time()
    for i in tqdm(range(num_updates), desc="Updating Documents"):
        collection.update_one({'index': i}, {'$set': {'timestamp': time.time()}})
    elapsed = time.time() - start_time
    print(f"Updated {num_updates} documents in {elapsed: .2f} seconds.")


def perform_deletes(db, num_deletes):
    """ Perform delete operations. """
    collection = db['test_data']
    start_time = time.time()
    for i in tqdm(range(num_deletes), desc="Deleting Documents"):
        collection.delete_one({'index': i})
    elapsed = time.time() - start_time
    print(f"Deleted {num_deletes} documents in {elapsed: .2f} seconds.")


def perform_bulk_inserts(db, num_documents, batch_size):
    """ Perform bulk insert operations. """
    collection = db['test_data']
    documents = [{'index': i, 'timestamp': time.time()} for i in range(num_documents)]
    start_time = time.time()
    for i in tqdm(range(0, num_documents, batch_size), desc="Bulk Inserting"):
        batch = documents[i:i + batch_size]
        collection.insert_many(batch)
    elapsed = time.time() - start_time
    print(f"Bulk inserted {num_documents} documents in {elapsed: .2f} seconds.")


def perform_complex_queries(db, num_queries):
    """ Perform complex read operations involving filters and sorting. """
    collection = db['test_data']
    start_time = time.time()
    for _ in tqdm(range(num_queries), desc="Complex Querying"):
        cursor = collection.find({'index': {'$lt': 500}}).sort('timestamp', -1)
        _ = list(cursor)
    elapsed = time.time() - start_time
    print(f"Performed {num_queries} complex queries in {elapsed: .2f} seconds.")


def concurrent_operations(db, function, num_operations, thread_count):
    """ Perform operations concurrently. """
    threads = []
    start_time = time.time()
    for _ in range(thread_count):
        thread = Thread(target=function, args=(db, num_operations // thread_count,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    elapsed = time.time() - start_time
    print(f"Concurrently performed {num_operations} operations in {elapsed: .2f} seconds using {thread_count} threads.")


def main():
    parser = argparse.ArgumentParser(description="MongoDB Benchmarking Tool")
    parser.add_argument('--host', type=str, default='localhost', help='MongoDB host')
    parser.add_argument('--port', type=int, default=27017, help='MongoDB port')
    parser.add_argument('--db', type=str, default='benchmark', help='Database name')
    parser.add_argument('--inserts', type=int, default=1000, help='Number of inserts')
    parser.add_argument('--reads', type=int, default=1000, help='Number of reads')
    parser.add_argument('--updates', type=int, default=1000, help='Number of updates')
    parser.add_argument('--deletes', type=int, default=1000, help='Number of deletes')
    parser.add_argument('--bulk-inserts', type=int, default=1000, help='Number of bulk inserts')
    parser.add_argument('--complex-queries', type=int, default=1000, help='Number of complex queries')
    parser.add_argument('--concurrency', type=int, default=10, help='Concurrency level for operations')

    args = parser.parse_args()

    db = connect_to_mongo(args.host, args.port, args.db)
    if db is not None:  # Change this line to properly check for a None object
        perform_inserts(db, args.inserts)
        perform_reads(db, args.reads)
        perform_updates(db, args.updates)
        perform_deletes(db, args.deletes)
        perform_bulk_inserts(db, args.bulk_inserts, 100)  # Assume a batch size of 100 for bulk inserts
        perform_complex_queries(db, args.complex_queries)
        concurrent_operations(db, perform_inserts, args.inserts, args.concurrency)


if __name__ == '__main__':
    main()
