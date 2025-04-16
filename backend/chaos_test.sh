#!/usr/bin/env bash
# Simulates agent failures across the stack

# 1. Randomly kill pods
kubectl get pods -n agentic --no-headers | awk '{print $1}' | xargs -I {} -n 1 -P 10   kubectl delete pod -n agentic {} --grace-period=0 --force &

# 2. Network latency injection
kubectl apply -f - <<EOF
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: agentic-latency-test
spec:
  action: delay
  mode: all
  selector:
    namespaces: [agentic]
  delay:
    latency: "500ms"
    correlation: "100"
EOF

# 3. Validate self-healing
echo "Waiting for recovery..."
while ! kubectl get deployment agentic-core -n agentic | grep "2/2"; do
  sleep 5
done
echo "System recovered!"
