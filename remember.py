from datetime import datetime

MEMORY_FILE = 'Memory Retention\Remembered.txt'

def toRemember(message):
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(MEMORY_FILE, 'a') as file:
        file.write(f"{date_time} - {message}\n")
    print(f"Memory saved: {message}")

def recall_memories(recent_only=False):
    try:
        with open(MEMORY_FILE, 'r') as file:
            memories = file.readlines()

        if not memories:
            print("No memories found.")
        else:
            if recent_only:
                recent_memory = memories[-1]  # Show only the most recently added memory
                print("Recently added memory:")
                print(recent_memory, end='')
            else:
                print("All stored memories:")
                print(*memories, sep='')
    except FileNotFoundError:
        print("No memories found.")
    except Exception as e:
        print(f"Error recalling memories: {e}")

if __name__ == "__main__":
    ch = input("Do you want me to remember something? (y/Y) ")
    if ch.lower() == 'y':
        toRemember(input("Let me know what you want me to remember...  "))

    choice = input("Do you want me to recite memories? Enter 1 to recite everything, or 2 for the most recent memory: ")
    if choice == '1':
        recall_memories()
    elif choice == '2':
        recall_memories(recent_only=True)
    else:
        print("Getting out of the program!!!!")
