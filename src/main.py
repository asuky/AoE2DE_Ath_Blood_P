from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId

import i18n

scn = AoE2DEScenario.from_file('../scenario/default0.aoe2scenario')

tm = scn.trigger_manager
um = scn.unit_manager

