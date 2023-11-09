from sklearn.ensemble import RandomForestRegressor

def formulate_strategy(data):
    model = RandomForestRegressor()
    X = data.drop('Close', axis=1)
    y = data['Close']
    model.fit(X, y)
    return model