

def DELETE_all_portfolios():
    
    portfolio_api = api_factory.build(lusid.api.PortfoliosApi)
    
    counter = 0
    
    for port in [port.id for port in  portfolio_api.list_portfolios().values]:
        
        try:
            portfolio_api.delete_portfolio(scope=port.scope, code=port.code)
            print(f"Portfolio {port.code} has been deleted from scope {port.scope}")
            counter +=1
        except:
            pass
        
    return f"Number of portfolios deleted is {counter}"
