from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import pytz
import lusid

api_factory = lusid.utilities.ApiClientFactory(
    api_secrets_filename=api_secrets_filename
)

port_group_args = [
    ["Finbourne-Examples", "Finbourne-Examples-Fund", "MultiAssetScope", "FUND_A"],
    ["Finbourne-Examples", "Finbourne-Examples-Fund", "MultiAssetScope", "FUND_B"],
]


def add_portfolio_to_group(group_scope, group_code, port_scope, port_code):
    return api_factory.build(lusid.api.PortfolioGroupsApi).add_portfolio_to_group(
        scope=group_scope,
        code=group_code,
        effective_at=datetime.now(tz=pytz.UTC),
        portfolio_id=lusid.models.ResourceId(scope=port_scope, code=port_code),
    )


executor = ThreadPoolExecutor()

futures = [
    executor.submit(
        add_portfolio_to_group,
        "Finbourne-Examples",
        "Finbourne-Examples-Fund",
        "MultiAssetScope",
        "FUND_A",
    ),
    executor.submit(
        add_portfolio_to_group,
        "Finbourne-Examples",
        "Finbourne-Examples-Fund",
        "MultiAssetScope",
        "FUND_B",
    ),
]

responses = [future.result() for future in futures]

print(responses)
