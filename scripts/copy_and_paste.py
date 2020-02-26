

## Add portfolio

api_factory.build(lusid.api.PortfolioGroupsApi).add_portfolio_to_group(scope="Finbourne-Examples",
                                                                       code="Finbourne-Examples-Fund",
                                                                       effective_at=datetime.now(tz=pytz.UTC),
                                                                       portfolio_id = lusid.models.ResourceId(scope="MultiAssetScope",
                                                                                                             code="FUND_A"))

## delete portfolio from group

api_factory.build(lusid.api.PortfolioGroupsApi).delete_portfolio_from_group(scope="Finbourne-Examples",
                                                                       code="Finbourne-Examples-Fund",
                                                                       effective_at=datetime.now(tz=pytz.UTC),
                                                                       portfolio_scope="MultiAssetScope",
                                                                       portfolio_code="FUND_A")