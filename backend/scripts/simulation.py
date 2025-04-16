from agent_forum import AgentForum

forum = AgentForum()

# Simulate agents submitting claims
forum.submit_argument("1001-2504-0034-6890", "Dorsal stream improves robotic arm precision", "Supported by neurocircuit data")
forum.submit_argument("3003-4506-2036-8892", "Visual memory loss impacts grip timing", "Observed delay in Segment_37")

resolved = forum.resolve_debates()
for r in resolved:
    print(f"{r['agent']} | {r['claim']} | Status: {r['status']}")
