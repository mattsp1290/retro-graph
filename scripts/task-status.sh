#!/bin/bash
# Quick task status checker

echo "=== Task Status Summary ==="
echo ""

# Count tasks by status
echo "Task Counts:"
echo "- Completed: $(grep -c "status: completed" proompts/tasks.yaml)"
echo "- In Progress: $(grep -c "status: in-progress" proompts/tasks.yaml)"
echo "- Pending: $(grep -c "status: pending" proompts/tasks.yaml)"
echo "- Blocked: $(grep -c "status: blocked" proompts/tasks.yaml)"

echo ""
echo "=== In-Progress Tasks ==="
awk '/- id:/{id=$3} /name:/{name=$0} /status: in-progress/{print id, name}' proompts/tasks.yaml

echo ""
echo "=== Next Available Tasks (pending with completed dependencies) ==="
# This is simplified - a more complex script would actually check dependencies
awk '/- id:/{id=$3} /name:/{name=$0} /status: pending/{if (!deps) print id, name} /dependencies:/{deps=1} /^ *- id:/{deps=0}' proompts/tasks.yaml | head -5
