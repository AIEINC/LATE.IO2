
import json

class AgentExecutionEngine:
    def __init__(self, agent):
        self.agent = agent

    def execute(self, env_input: dict):
        decision = self.agent.decide_behavior(env_input)
        result = {
            "agent_id": self.agent.agent_id,
            "input": env_input,
            "decision": decision,
            "log_entry": self._log_to_memory(env_input, decision)
        }
        return result

    def _log_to_memory(self, input_data, decision):
        memory_path = f"memory/{self.agent.agent_id}_memory.csv"
        try:
            with open(memory_path, "a") as f:
                f.write(f"{json.dumps(input_data)},{json.dumps(decision)}\n")
            return f"Memory updated: {memory_path}"
        except Exception as e:
            return f"Memory log failed: {str(e)}"
