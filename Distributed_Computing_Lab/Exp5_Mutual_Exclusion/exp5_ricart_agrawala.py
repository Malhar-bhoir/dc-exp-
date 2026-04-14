import threading
import time

class RicartAgrawala:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.timestamp = 0
        self.request_queue = []
        self.replies_received = 0
        self.lock = threading.Lock()
        self.terminated = False

    def request_critical_section(self):
        with self.lock:
            self.timestamp += 1
            print(f"Process {self.process_id} requesting CS at time {self.timestamp}")
            self.request_queue.append((self.timestamp, self.process_id))
            return self.timestamp

    def receive_request(self, timestamp, process_id):
        with self.lock:
            self.timestamp = max(self.timestamp, timestamp) + 1
            print(f"Process {self.process_id} received request from {process_id} at time {timestamp}")
            self.send_reply(process_id)

    def send_reply(self, process_id):
        print(f"Process {self.process_id} sends reply to Process {process_id}")

    def receive_reply(self):
        self.replies_received += 1

    def execute_critical_section(self):
        while self.replies_received < self.num_processes - 1:
            time.sleep(0.5) # Wait for replies
        print(f"Process {self.process_id} enters CS")
        time.sleep(1)
        print(f"Process {self.process_id} exits CS")
        self.terminate()

    def terminate(self):
        self.terminated = True
        print(f"Process {self.process_id} has finished execution.")

if __name__ == "__main__":
    processes = [RicartAgrawala(i, 3) for i in range(3)]

    timestamps = [p.request_critical_section() for p in processes]

    for i in range(3):
        for j in range(3):
            if i != j:
                processes[j].receive_request(timestamps[i], i)

    for i in range(3):
        for j in range(3):
            if i != j:
                processes[i].receive_reply()

    for p in processes:
        p.execute_critical_section()