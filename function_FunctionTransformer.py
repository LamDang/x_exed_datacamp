def contract_seniority(X):
    # get the days instead of ns
    return ((X['Claim Incident date'] - X['Initial coverage date']).values.astype(float) / 1e9).reshape(-1, 1)
def time_to_declaration(X):
    # get the days instead of ns
    return ((X['FE_Declaration_date'] - X['Claim Incident date']).values.astype(float) / 1e9).reshape(-1, 1)