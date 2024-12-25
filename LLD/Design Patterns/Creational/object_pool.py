"""
Use case: Where we need a pool of objects that can be reuse it, like db connection object
someone asks from the pool, uses it, then returns it

Should be used with singleton + thread safety to not allow multiple pool creations.
"""

import threading
import queue
import time


class DatabaseConnection:
    """Simulates a database connection."""
    def __init__(self, connection_id):
        self.connection_id = connection_id

    def execute_query(self, query):
        print(f"[Connection {self.connection_id}] Executing query: {query}")


class DatabaseConnectionPool:
    """Thread-safe Database Connection Pool using Singleton pattern."""
    _instance = None
    _lock = threading.Lock()  # Lock for thread-safe singleton

    def __new__(cls, max_connections=5):
        with cls._lock:  # Ensure thread safety when creating a singleton
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, max_connections=5):
        if not self._initialized:
            self._max_connections = max_connections
            self._available_connections = queue.Queue(max_connections)
            self._used_connections = set()
            self._lock = threading.Lock()

            # Create a pool of database connections
            for i in range(max_connections):
                self._available_connections.put(DatabaseConnection(i + 1))

            self._initialized = True

    def acquire_connection(self):
        """Acquire a connection from the pool."""
        with self._lock:
            if not self._available_connections.empty():
                conn = self._available_connections.get()
                self._used_connections.add(conn)
                print(f"[INFO] Acquired Connection {conn.connection_id}")
                return conn
            else:
                print("[WARN] No available connections. Waiting...")
                while self._available_connections.empty():
                    time.sleep(0.1)
                return self.acquire_connection()

    def release_connection(self, conn):
        """Release a connection back to the pool."""
        with self._lock:
            if conn in self._used_connections:
                self._used_connections.remove(conn)
                self._available_connections.put(conn)
                print(f"[INFO] Released Connection {conn.connection_id}")
            else:
                print(f"[WARN] Attempted to release a connection not in use: {conn.connection_id}")


# Usage Example
def worker_task(pool, task_id):
    """Simulates a worker using a connection from the pool."""
    conn = pool.acquire_connection()
    conn.execute_query(f"SELECT * FROM tasks WHERE task_id = {task_id}")
    time.sleep(1)  # Simulating query execution time
    pool.release_connection(conn)


if __name__ == "__main__":
    # Create a single connection pool (singleton)
    pool = DatabaseConnectionPool(max_connections=3)

    # Simulate multiple threads accessing the pool
    threads = []
    for i in range(6):  # More threads than available connections
        thread = threading.Thread(target=worker_task, args=(pool, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
