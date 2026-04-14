import threading
import time
import queue

class LamportMutex:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.clock = 0
        self.request_queue = queue.PriorityQueue()
        self.reply_count = 0
        self.lock = threading.Lock()
        self.terminated = False

    def send_request(self):
        with self.lock:
            self.clock += 1
            timestamp = self.clock
            print(f"Process {self.process_id} sends request at time {timestamp}")
            self.request_queue.put((timestamp, self.process_id))
            return timestamp

    def receive_request(self, timestamp, process_id):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1
            print(f"Process {self.process_id} received request from {process_id} at time {timestamp}")
            self.send_reply(process_id)

    def send_reply(self, process_id):
        print(f"Process {self.process_id} sends reply to Process {process_id}")

    def receive_reply(self):
        self.reply_count += 1

    def execute_critical_section(self):
        while self.reply_count < self.num_processes - 1:
            time.sleep(0.5) # Wait for replies
        print(f"Process {self.process_id} enters CS")
        time.sleep(1)
        print(f"Process {self.process_id} exits CS")
        self.terminate()

    def terminate(self):
        self.terminated = True
        print(f"Process {self.process_id} has finished execution.")

if __name__ == "__main__":
    # Simulating for 3 processes
    processes = [LamportMutex(i, 3) for i in range(3)]

    # Sending requests
    timestamps = [p.send_request() for p in processes]

    for i in range(3):
        for j in range(3):
            if i != j:
                processes[j].receive_request(timestamps[i], i)

    # Receiving replies
    for i in range(3):
        for j in range(3):
            if i != j:
                processes[i].receive_reply()

    for p in processes:
        p.execute_critical_section()