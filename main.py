class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def display(self):
        print(self.queue)


class QueueSystem:
    def __init__(self):
        self.queues = {}

    def create_queue(self, name):
        if name not in self.queues:
            self.queues[name] = Queue()

    def delete_queue(self, name):
        if name in self.queues:
            del self.queues[name]

    def enqueue_item(self, queue_name, item):
        if queue_name in self.queues:
            self.queues[queue_name].enqueue(item)

    def dequeue_item(self, queue_name):
        if queue_name in self.queues:
            return self.queues[queue_name].dequeue()
        else:
            return None

    def get_queue_size(self, queue_name):
        if queue_name in self.queues:
            return self.queues[queue_name].size()
        else:
            return 0

    def peek_queue(self, queue_name):
        if queue_name in self.queues:
            return self.queues[queue_name].peek()
        else:
            return None

    def display_queues(self):
        for queue_name, queue in self.queues.items():
            print(f"Queue {queue_name}: {queue.display()}")


def main():
    queue_system = QueueSystem()
    while True:
        print("1. Create queue")
        print("2. Delete queue")
        print("3. Enqueue item")
        print("4. Dequeue item")
        print("5. Get queue size")
        print("6. Peek queue")
        print("7. Display queues")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter queue name: ")
            queue_system.create_queue(name)
        elif choice == "2":
            name = input("Enter queue name: ")
            queue_system.delete_queue(name)
        elif choice == "3":
            queue_name = input("Enter queue name: ")
            item = input("Enter item: ")
            queue_system.enqueue_item(queue_name, item)
        elif choice == "4":
            queue_name = input("Enter queue name: ")
            print(queue_system.dequeue_item(queue_name))
        elif choice == "5":
            queue_name = input("Enter queue name: ")
            print(queue_system.get_queue_size(queue_name))
        elif choice == "6":
            queue_name = input("Enter queue name: ")
            print(queue_system.peek_queue(queue_name))
        elif choice == "7":
            queue_system.display_queues()
        elif choice == "8":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()