from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import Operation

import consts
import vars
import i18n

class Counter:
    
    @staticmethod
    def add_enemy_kill_counter(tm: TriggerManager) -> None: 
        i = i18n
        for killed_player in PlayerId.all(exclude_gaia = True):
            for by_player in PlayerId.all(exclude_gaia = True):

                # 倒した数カウンターをある程度の単位で分ける。
                # 複数のユニットを砲撃や範囲攻撃で倒したとき、1 ユニット単位でしか扱えないと
                # まとめて倒した数と同じだけの時間が掛かるため。
                # 
                # これを 1 ユニット単位でしか作らなかった場合、トリガは毎秒 1 回ずつしか処理されないので、
                # 例えば 50 ユニットまとめて潰したらゲーム内 50 秒掛かることになる。
                # もう少し言えばシナリオの勝利条件とかをキル数で設定するような場合、その時間分だけ勝利処理が遅れることになる。
                # さらにトリガは上から実行されるので、大きい数の方を先に作らないと、
                # 小さい数の方が先に処理されてしまい、やはり処理が遅れることになる。

                # Creating triggers for each "number of units"
                # For treating as many units at once, such as units killed by siege or trample.
                # If those are not, counter takes as many seconds as units (50 unit kills = takes 50 secs),
                # and results delaying archivements in whole game.
                # 
                # This must be ordered by descend. If smaller value is prior to larger, 
                # this always runs "smaller number" trigger first and takes more time to process.
                for num_units in [50, 10, 5, 1]:

                    # ユニット倒された人＝ユニット倒した人、つまり投石とかで自キルしたケースを排除
                    # Ignoring cases that killed = by (self-killing using such as mangonels etc)
                    if (killed_player == by_player):
                        continue
                    
                    # 倒した人の倒した数が上がったとき（倒した数は「資源」扱いである点に注意）
                    # When "by player" kills "killed player" units
                    t = tm.add_trigger("[%s] p%d %d killed by p%d" % (__class__.__name__, killed_player.value, num_units, by_player.value))
                    t.looping = True
                    t.new_condition.accumulate_attribute(
                        num_units,
                        consts.NUM_OF_KILLS[by_player],
                        killed_player,
                        None
                    )

                    # ユニット倒された人と、ユニット倒した人が同盟でない、つまり味方投石等でキル取ったケースを排除
                    # and "killed player" is not allied with "by player"
                    # (prevents ally-killing)
                    t.new_condition.diplomacy_state(
                        consts.DIPLO_ALLY,
                        killed_player,
                        consts.NOT,
                        by_player
                    )

                    # 資源の「プレイヤー x に倒された数」を規定数減らす。
                    # このカウンタは、倒した対象が敵か味方か区別しないので、ゲーム内の変数機能を代理で使って記録する
                    # Decreasing attribute(resource) of "KILLS BY 'by_player'".
                    # This attribute does not distinguish killed unit is ally or not.
                    # Thus this scenario has own kills counter using in-game variable instead.
                    t.new_effect.modify_resource(
                        num_units,
                        consts.NUM_OF_KILLS[by_player],
                        killed_player,
                        Operation.SUBTRACT
                    )

                    # 自キル・味方キルでない場合は倒した数として、ゲーム内の変数機能を使って記録する
                    # Increasing own kills counter of 'by_player'.
                    # This variable will be used everywhere those handle archivements by number of kills.
                    t.new_effect.change_variable(
                        num_units,
                        Operation.ADD,
                        vars.ENEMY_KILLS + by_player.value - 1,
                        i._("vars_KillsCounter") % by_player.value
                    )
