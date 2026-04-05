import asyncio
from env.env import SupportInboxEnv
from env.models import Action

MAX_STEPS = 5

def log_start(task):
    print(f"[START] task={task} env=support_env model=baseline", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}", flush=True)

def decide_action(msg):
    msg = msg.lower()
    if "refund" in msg or "charged" in msg:
        return Action(action_type="refund", refund_amount=20.0, message="Refund issued")
    elif "delay" in msg:
        return Action(action_type="reply", message="Sorry for delay")
    else:
        return Action(action_type="escalate", message="Escalating")

async def run_task(task):
    env = SupportInboxEnv(task)
    rewards = []
    result = await env.reset()

    log_start(task)

    for step in range(1, MAX_STEPS + 1):
        obs = result["observation"]

        action = decide_action(obs.customer_message)

        result = await env.step(action)

        reward = result["reward"]
        done = result["done"]

        rewards.append(reward)

        log_step(step, action.action_type, reward, done)

        if done:
            break

    success = sum(rewards) > 0.5
    log_end(success, step, rewards)

async def main():
    for task in ["easy", "medium", "hard"]:
        await run_task(task)

if __name__ == "__main__":
    asyncio.run(main())