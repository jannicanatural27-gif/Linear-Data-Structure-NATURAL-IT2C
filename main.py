class DynamicQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    enqueue = lambda self, item: (self.queue.append(item), print(f"'{item}' added to queue."))[1]

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! No elements to remove.")
            return None
        removed = self.queue.pop(0)
        print(f"'{removed}' removed from queue.")
        return removed

    def display(self):
        print("Current Queue (Front to Rear):", self.queue)


# Interactive Execution
if __name__ == "__main__":
    my_queue = DynamicQueue()
    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            val = input("Enter value to enqueue: ")
            my_queue.enqueue(val)
        elif choice == '2':
            my_queue.dequeue()
        elif choice == '3':
            my_queue.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")