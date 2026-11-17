# Logan Latimer - Assignment 4

def check_session(idle_minutes, max_idle=30):
    # TODO: Evaluate idle time against max_idle threshold
    # Note: Check the default parameter value above against what the system requires!
    if idle_minutes<max_idle:
        return "SESSION_ACTIVE"
    else: 
        return "SESSION_EXPIRED"