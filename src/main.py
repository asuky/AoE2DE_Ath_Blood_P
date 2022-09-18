from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

import i18n
import consts

from counters import Counter

# Scenario folder is mounted on ../scenario by docker.
# Copying built file to scenario folder everytime is toil...
scn = AoE2DEScenario.from_file('../scenario/default0.aoe2scenario')
i = i18n

tm = scn.trigger_manager
um = scn.unit_manager

Counter.add_enemy_kill_counter(tm)

scn.write_to_file('../scenario/Ath_Blood_P_' + consts.VERSION + '.aoe2scenario')