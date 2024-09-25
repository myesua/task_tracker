from classes.name import TaskAdmin
from config.env import Config
from handlers.parser import parse_args

def main():
    args = parse_args()
    task_admin = TaskAdmin(Config().TASKS_FILE)
    
    task_admin.add_task(args.description) if args.command == 'add' and args.description else task_admin.update_task(args.task_id, args.description) if args.command == 'update' and args.description and args.task_id else task_admin.delete_task(args.task_id) if args.command == 'delete' and args.task_id else task_admin.list_tasks(args.status) if args.command == 'list' else task_admin.mark_in_progress(args.task_id) if args.command == 'mark-in-progress' and args.task_id else task_admin.mark_as_done(args.task_id) if args.command == 'mark-done' and args.task_id else print('Invalid command or argument. Use -h for help')

# Main Execution
if __name__ == "__main__":
    main()
    
    
    