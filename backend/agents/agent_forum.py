class AgentForum:
    def __init__(self):
        self.debates = []
    
    def submit_argument(self, agent_id, claim, evidence):
        self.debates.append({
            "agent": agent_id,
            "claim": claim,
            "evidence": evidence,
            "status": "pending"
        })

    def resolve_debates(self):
        for debate in self.debates:
            if "neurocircuit" in debate["evidence"].lower():
                debate["status"] = "approved"
            else:
                debate["status"] = "needs_more_evidence"
        return self.debates
