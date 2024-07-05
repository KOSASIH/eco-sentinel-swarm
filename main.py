import os
import json
from config import Config
from sentinel import Sentinel
from swarm import Swarm
from intelligence import AI, ML, DL
from infrastructure import Cloud, OnPrem
from monitoring import Logging, Tracing, Alerting
from security import Auth, IAM, RBAC
from testing import UnitTesting, IntegrationTesting, E2ETesting
from utils import Math, Stats, Geo
from web import API, UI

def main():
    config = Config()
    sentinel = Sentinel(config)
    swarm = Swarm(config)
    ai = AI(config)
    ml = ML(config)
    dl = DL(config)
    cloud = Cloud(config)
    on_prem = OnPrem(config)
    logging = Logging(config)
    tracing = Tracing(config)
    alerting = Alerting(config)
    auth = Auth(config)
    iam = IAM(config)
    rbac = RBAC(config)
    unit_testing = UnitTesting(config)
    integration_testing = IntegrationTesting(config)
    e2e_testing = E2ETesting(config)
    math = Math(config)
    stats = Stats(config)
    geo = Geo(config)
    api = API(config)
    ui = UI(config)

    # Initialize the system
    sentinel.init()
    swarm.init()
    ai.init()
    ml.init()
    dl.init()
    cloud.init()
    on_prem.init()
    logging.init()
    tracing.init()
    alerting.init()
    auth.init()
    iam.init()
    rbac.init()
    unit_testing.init()
    integration_testing.init()
    e2e_testing.init()
    math.init()
    stats.init()
    geo.init()
    api.init()
    ui.init()

    # Start the system
    sentinel.start()
    swarm.start()
    ai.start()
    ml.start()
    dl.start()
    cloud.start()
    on_prem.start()
    logging.start()
    tracing.start()
    alerting.start()
    auth.start()
    iam.start()
    rbac.start()
    unit_testing.start()
    integration_testing.start()
    e2e_testing.start()
    math.start()
    stats.start()
    geo.start()
    api.start()
    ui.start()

if __name__ == "__main__":
    main()
