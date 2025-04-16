class Agent:
    def __init__(self, id, role, target_env, dependencies, trigger):
        self.id = id
        self.role = role
        self.env = target_env
        self.dependencies = dependencies
        self.trigger = trigger

    def evaluate_trigger(self, metrics):
        return self.trigger(metrics)