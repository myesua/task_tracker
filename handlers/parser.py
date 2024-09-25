import argparse

# Function to Parse Command-Line Arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # Subparser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Command to run (add). Add new task")
    add_parser.add_argument('description', type=str, help="Description of the task. To be on the safer side, put description in quote.")
    
    # Subparser for the 'update' command
    update_parser = subparsers.add_parser("update", help="Command to run (update). Update a task")
    update_parser.add_argument('task_id', type=int, help="ID of the task to update")
    update_parser.add_argument('description', type=str, help="Description of the task. To be on the safer side, put description in quote.")
    
    list_parser = subparsers.add_parser("list", help="Command to run (list). List all tasks")
    list_parser.add_argument("status", nargs='?', choices=['done', 'todo', 'in-progress'], type=str, help="Command to run ('list done', 'list todo', or 'list in-progress')")
    
    # Subparser for the 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Command to run (update). Update a task")
    delete_parser.add_argument('task_id', type=int, help="ID of the task to update") 
    
    mark_as_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Command to run (mark-in-progress). Mark a task as in progress")
    mark_as_in_progress_parser.add_argument('task_id', type=int, help="ID of the task to update")
    
    mark_as_done_parser = subparsers.add_parser("mark-done", help="Command to run (mark-done). Mark a task as done")
    mark_as_done_parser.add_argument('task_id', type=int, help="ID of the task to update")  
    
    return parser.parse_args()
