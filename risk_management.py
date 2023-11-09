def calculate_risk(trade):
    entry_price = trade['entry_price']
    stop_loss = trade['stop_loss']
    take_profit = trade['take_profit']
    risk_reward_ratio = (entry_price - stop_loss) / (take_profit - entry_price)
    return risk_reward_ratio

def ask_permission(risk):
    if risk > 1/3 or risk > 0.05:
        return False
    return True

def main():
    pass

if __name__ == "__main__":
    main()