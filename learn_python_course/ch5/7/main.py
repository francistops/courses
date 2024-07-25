def unlock_achievement(before_xp, ach_xp, ach_name):
    xp = before_xp + ach_xp
    ach_msg = f"Achievement Unlocked: {ach_name}"
    return xp, ach_msg
