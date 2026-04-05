def grade_step(task, action, history):
    expected = task["expected"]

    reward = 0.0
    done = False

    if action.action_type == expected:
        reward += 0.6

    if action.message:
        reward += 0.2

    if action.action_type == "refund" and action.refund_amount:
        reward += 0.2

    if action.action_type not in ["reply", "refund", "escalate"]:
        reward -= 0.5

    reward = max(0.0, min(1.0, reward))

    if reward >= 0.8:
        done = True

    return reward, done, {"expected": expected}