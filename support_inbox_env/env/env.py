from .models import Observation, Action
from .tasks import load_task
from .graders import grade_step

class SupportInboxEnv:

    def __init__(self, task_name="easy"):
        self.task_name = task_name
        self.task = load_task(task_name)
        self.history = []
        self.done = False
        self.step_count = 0

    async def reset(self):
        self.task = load_task(self.task_name)
        self.history = []
        self.done = False
        self.step_count = 0

        return {
            "observation": Observation(
                ticket_id=self.task["id"],
                customer_message=self.task["message"],
                history=[],
                status="open"
            ),
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    async def step(self, action: Action):
        self.step_count += 1

        reward, done, info = grade_step(self.task, action, self.history)

        self.history.append(action.action_type)
        self.done = done

        return {
            "observation": Observation(
                ticket_id=self.task["id"],
                customer_message=self.task["message"],
                history=self.history,
                status="resolved" if done else "open"
            ),
            "reward": reward,
            "done": done,
            "info": info
        }

    def state(self):
        return {
            "task": self.task_name,
            "history": self.history,
            "steps": self.step_count,
            "done": self.done
        }