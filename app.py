from src.setup import Setup

init_str = """
###############
Task List CLI
###############
Options:
{options}
###############
{pending_tasks}
"""

def init() -> None:
    setup = Setup()
    
    print(init_str.format(
            options=setup.get_options(), 
            pending_tasks=setup.get_pending_tasks()
        )
    )
    setup.get_user_input()

if __name__ == '__main__':
    init()
