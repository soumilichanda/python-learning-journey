from collections import deque
from typing import Callable


class TaskNode:
    """Represents a discrete task node in an execution dependency tree."""

    def __init__(self, task_id: str, action: Callable[[], str]):
        self.task_id = task_id
        self.action = action
        self.dependencies: list["TaskNode"] = []

    def add_dependency(self, child: "TaskNode") -> None:
        self.dependencies.append(child)


class TaskSchedulerEngine:
    """Executes hierarchical tasks level by level with rollbacks using stack invariants."""

    def __init__(self):
        self.executed_history: list[str] = []
        self.rollback_stack: list[str] = []

    def execute_hierarchy(self, root: TaskNode) -> list[str]:
        queue: deque[TaskNode] = deque([root])
        execution_order: list[str] = []

        while queue:
            node = queue.popleft()
            status = node.action()
            execution_order.append(f"{node.task_id} -> {status}")
            self.executed_history.append(node.task_id)
            self.rollback_stack.append(node.task_id)

            for child in node.dependencies:
                queue.append(child)

        return execution_order

    def rollback_last_n(self, count: int) -> list[str]:
        rolled_back: list[str] = []
        for _ in range(min(count, len(self.rollback_stack))):
            task = self.rollback_stack.pop()
            rolled_back.append(task)
        return rolled_back


if __name__ == "__main__":
    t_root = TaskNode("Init_Pipeline", lambda: "SUCCESS")
    t_data = TaskNode("Ingest_Data", lambda: "SUCCESS")
    t_prep = TaskNode("Preprocess", lambda: "SUCCESS")
    t_train = TaskNode("Train_Model", lambda: "SUCCESS")

    t_root.add_dependency(t_data)
    t_root.add_dependency(t_prep)
    t_prep.add_dependency(t_train)

    scheduler = TaskSchedulerEngine()
    print("=== Milestone 3: Task Scheduler & Rollback Engine ===")
    run_log = scheduler.execute_hierarchy(t_root)
    for entry in run_log:
        print(f"Run: {entry}")

    reverted = scheduler.rollback_last_n(2)
    print(f"\nRolled back recent operations (LIFO): {reverted}")