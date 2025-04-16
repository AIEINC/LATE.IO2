import json
import logging
from datetime import datetime
from pathlib import Path
from agents.learning_loop import query_knowledge_base

class LoopManager:
    def __init__(self, agent_name):
        self.agent = agent_name
        self.log_dir = Path(f"/opt/agentic/logs/feedback/{datetime.now().strftime('%Y-%m-%d')}")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            filename=self.log_dir / f"{self.agent}_loop_debug.log",
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )

    def run_loop(self, initial_input):
        loop_id = datetime.now().strftime("%H%M%S")
        logging.info(f"Starting feedback loop: {loop_id}")

        phase1 = self._generate_output(initial_input)
        self._log_phase(loop_id, 1, phase1)

        phase2 = self._reflect(phase1, cycle=1)
        self._log_phase(loop_id, 2, phase2)

        phase3 = self._reflect(phase2, cycle=2)
        self._log_phase(loop_id, 3, phase3)

        phase4 = self._research(phase3)
        self._log_phase(loop_id, 4, phase4)

        final = self._finalize(phase4)
        self._log_phase(loop_id, 5, final, is_final=True)

        logging.info(f"Completed feedback loop: {loop_id}")
        return final

    def _log_phase(self, loop_id, phase_num, data, is_final=False):
        log_file = self.log_dir / f"{self.agent}_{loop_id}.json"
        phase_key = "final" if is_final else f"phase_{phase_num}"

        try:
            if log_file.exists():
                with open(log_file, 'r+') as f:
                    log_data = json.load(f)
                    log_data[phase_key] = data
                    f.seek(0)
                    json.dump(log_data, f, indent=2)
                    f.truncate()
            else:
                with open(log_file, 'w') as f:
                    json.dump({phase_key: data}, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to log phase {phase_num}: {str(e)}")

    def _generate_output(self, task_input):
        return {
            "input": task_input,
            "output": f"Initial output for: {task_input}",
            "meta": {"agent": self.agent, "stage": "initial"}
        }

    def _reflect(self, previous_output, cycle):
        text = previous_output.get("output", "")
        reflection = f"Reflection {cycle} applied to: {text}"
        return {
            "input": text,
            "output": reflection,
            "meta": {
                "agent": self.agent,
                "stage": f"reflection_{cycle}",
                "notes": f"Refined for clarity and impact, pass {cycle}"
            }
        }

    def _research(self, refined_output):
        query = refined_output.get("output", "")
        inspiration = query_knowledge_base(query)
        integrated = f"{refined_output['output']} + Research Applied: {inspiration}"
        return {
            "input": query,
            "output": integrated,
            "meta": {
                "agent": self.agent,
                "stage": "research",
                "source": "internal_kb"
            }
        }

    def _finalize(self, researched_output):
        summary = researched_output.get("output", "")
        return {
            "input": researched_output["input"],
            "output": summary,
            "meta": {
                "agent": self.agent,
                "stage": "final",
                "timestamp": datetime.now().isoformat()
            }
        }