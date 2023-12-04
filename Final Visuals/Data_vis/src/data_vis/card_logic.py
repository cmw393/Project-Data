import random
class CardLogic:
    @staticmethod
    def knight_logic():
        base_damage = random.randint(8, 15)
        return {'damage': base_damage}
    @staticmethod
    def archers_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}
    @staticmethod
    def goblins_logic():
        base_damage = random.randint(6, 14)
        return {'damage': base_damage}
    @staticmethod
    def giant_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def pekka_logic():
        base_damage = random.randint(20, 35)
        return {'damage': base_damage}
    @staticmethod
    def minions_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}
    @staticmethod
    def balloon_logic():
        base_damage = random.randint(50, 80)
        return {'damage': base_damage}
    @staticmethod
    def witch_logic():
        base_damage = random.randint(20, 30)
        spawn_skeletons_chance = random.random()  # 50% chance of spawning skeletons
        return {'damage': base_damage, 'spawn_skeletons': spawn_skeletons_chance < 0.5}
    @staticmethod
    def barbarians_logic():
        base_damage = random.randint(10, 20)
        return {'damage': base_damage}
    @staticmethod
    def golem_logic():
        base_damage = random.randint(30, 50)
        return {'damage': base_damage}
    @staticmethod
    def skeletons_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}
    @staticmethod
    def valkyrie_logic():
        base_damage = random.randint(10, 18)
        return {'damage': base_damage}
    @staticmethod
    def skeleton_army_logic():
        base_damage_per_skeleton = random.randint(6, 12)  # Set the amount of damage each skeleton does
        num_skeletons = random.randint(5, 15)  # Set the range for the number of skeletons to spawn
        total_damage = base_damage_per_skeleton * num_skeletons
        return {'damage': total_damage, 'num_skeletons': num_skeletons}
    @staticmethod
    def bomber_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def musketeer_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def baby_dragon_logic():
        base_damage = random.randint(10, 20)
        return {'damage': base_damage}
    @staticmethod
    def prince_logic():
        base_damage = random.randint(20, 35)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}
    @staticmethod
    def wizard_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}
    @staticmethod
    def mini_pekka_logic():
        base_damage = random.randint(10, 20)
        return {'damage': base_damage}
    @staticmethod
    def spear_goblins_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}
    @staticmethod
    def giant_skeleton_logic():
        base_damage = random.randint(25, 40)
        return {'damage': base_damage}
    @staticmethod
    def hog_rider_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def minion_horde_logic():
        base_damage = random.randint(30, 50)
        return {'damage': base_damage}
    @staticmethod
    def ice_wizard_logic():
        base_damage = random.randint(5, 12)
        slow_chance = random.random()  # 40% chance of slowing down the opponent
        return {'damage': base_damage, 'slow': slow_chance < 0.4}
    @staticmethod
    def royal_giant_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}
    @staticmethod
    def guards_logic():
        base_damage = random.randint(5, 12)
        shielded = random.random()  # 50% chance of having a shield
        return {'damage': base_damage, 'shielded': shielded < 0.5}
    @staticmethod
    def princess_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}
    @staticmethod
    def dark_prince_logic():
        base_damage = random.randint(15, 25)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}
    @staticmethod
    def three_musketeers_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def lava_hound_logic():
        base_damage = random.randint(5, 12)
        pups_spawn_chance = random.random()  # 80% chance of spawning pups
        return {'damage': base_damage, 'spawn_pups': pups_spawn_chance < 0.8}
    @staticmethod
    def ice_spirit_logic():
        freeze_chance = random.random()  # 20% chance of freezing the opponent
        return {'damage': 0, 'freeze': freeze_chance < 0.2}
    @staticmethod
    def fire_spirits_logic():
        splash_damage = random.randint(50, 80)
        return splash_damage
    @staticmethod
    def miner_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}
    @staticmethod
    def sparky_logic():
        base_damage = random.randint(50, 100)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}
    @staticmethod
    def bowler_logic():
        base_damage = random.randint(25, 40)
        return {'damage': base_damage}
    @staticmethod
    def lumberjack_logic():
        base_damage = random.randint(10, 20)
        rage_chance = random.random()  # 40% chance of dropping a rage spell
        return {'damage': base_damage, 'rage': rage_chance < 0.4}
    @staticmethod
    def ice_golem_logic():
        base_damage = random.randint(20, 30)
        slow_chance = random.random()  # 50% chance of slowing down the opponent
        death_freeze_chance = random.random()  # 30% chance of triggering Death Freeze
        return {'damage': base_damage, 'slow': slow_chance < 0.5, 'death_freeze': death_freeze_chance < 0.3}

    @staticmethod
    def battle_ram_logic():
        base_damage = random.randint(20, 35)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}
    @staticmethod
    def inferno_dragon_logic():
        base_damage = random.randint(10, 20)
        charge_bonus = random.random()  # 30% chance of charging
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}
    @staticmethod
    def cannon_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}
    @staticmethod
    def firecracker_logic():
        base_damage = random.randint(50, 80)
        return {'damage': base_damage}
    @staticmethod
    def mega_minion_logic():
        base_damage = random.randint(10, 20)
        return {'damage': base_damage}

    @staticmethod
    def dart_goblin_logic():
        base_damage = random.randint(5, 15)
        return {'damage': base_damage}

    @staticmethod
    def goblin_gang_logic():
        base_damage = random.randint(10, 18)
        return {'damage': base_damage}

    @staticmethod
    def electro_wizard_logic():
        base_damage = random.randint(15, 25)
        spawn_stun_chance = random.random()  # 50% chance of spawning a stun effect
        return {'damage': base_damage, 'spawn_stun': spawn_stun_chance < 0.5}

    @staticmethod
    def elite_barbarians_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}

    @staticmethod
    def hunter_logic():
        base_damage = random.randint(8, 15)
        return {'damage': base_damage}

    @staticmethod
    def executioner_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}

    @staticmethod
    def bandit_logic():
        base_damage = random.randint(20, 35)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}

    @staticmethod
    def royal_recruits_logic():
        base_damage = random.randint(5, 10)
        return {'damage': base_damage}

    @staticmethod
    def night_witch_logic():
        base_damage = random.randint(5, 15)
        spawn_bats_chance = random.random()  # 70% chance of spawning bats
        return {'damage': base_damage, 'spawn_bats': spawn_bats_chance < 0.7}

    @staticmethod
    def bats_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}

    @staticmethod
    def royal_ghost_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}

    @staticmethod
    def ram_rider_logic():
        base_damage = random.randint(15, 25)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}

    @staticmethod
    def zappies_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}
    
    @staticmethod
    def rascals_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}

    @staticmethod
    def cannon_cart_logic():
        base_damage = random.randint(10, 18)
        return {'damage': base_damage}

    @staticmethod
    def mega_knight_logic():
        base_damage = random.randint(20, 35)
        spawn_jump_chance = random.random()  # 30% chance of spawning jump effect
        return {'damage': base_damage, 'spawn_jump': spawn_jump_chance < 0.3}

    @staticmethod
    def skeleton_barrel_logic():
        base_damage = random.randint(5, 12)
        spawn_skeletons_chance = random.random()  # 80% chance of spawning skeletons
        return {'damage': base_damage, 'spawn_skeletons': spawn_skeletons_chance < 0.8}

    @staticmethod
    def flying_machine_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}

    @staticmethod
    def wall_breakers_logic():
        base_damage = random.randint(10, 20)
        return {'damage': base_damage}

    @staticmethod
    def royal_hogs_logic():
        base_damage = random.randint(15, 25)
        return {'damage': base_damage}

    @staticmethod
    def goblin_giant_logic():
        base_damage = random.randint(20, 30)
        return {'damage': base_damage}

    @staticmethod
    def fisherman_logic():
        base_damage = random.randint(8, 15)
        return {'damage': base_damage}

    @staticmethod
    def magic_archer_logic():
        base_damage = random.randint(10, 20)
        pierce_through_chance = random.random()  # 40% chance of piercing through
        return {'damage': base_damage, 'pierce_through': pierce_through_chance < 0.4}

    @staticmethod
    def electro_dragon_logic():
        base_damage = random.randint(20, 30)
        chain_lightning_chance = random.random()  # 50% chance of chain lightning
        return {'damage': base_damage, 'chain_lightning': chain_lightning_chance < 0.5}

    @staticmethod
    def elixir_golem_logic():
        base_damage = random.randint(5, 12)
        elixir_spawn_chance = random.random()  # 80% chance of spawning elixir on defeat
        return {'damage': base_damage, 'elixir_spawn': elixir_spawn_chance < 0.8}

    @staticmethod
    def battle_healer_logic():
        base_damage = random.randint(5, 15)
        heal_allies_chance = random.random()  # 60% chance of healing nearby allies
        return {'damage': base_damage, 'heal_allies': heal_allies_chance < 0.6}

    @staticmethod
    def skeleton_dragons_logic():
        base_damage = random.randint(10, 20)
        spawn_baby_dragons_chance = random.random()  # 50% chance of spawning baby dragons
        return {'damage': base_damage, 'spawn_baby_dragons': spawn_baby_dragons_chance < 0.5}

    @staticmethod
    def mother_witch_logic():
        base_damage = random.randint(10, 18)
        spawn_piglets_chance = random.random()  # 70% chance of spawning piglets
        return {'damage': base_damage, 'spawn_piglets': spawn_piglets_chance < 0.7}

    @staticmethod
    def electro_spirit_logic():
        base_damage = random.randint(5, 12)
        return {'damage': base_damage}

    @staticmethod
    def electro_giant_logic():
        base_damage = random.randint(25, 35)
        spawn_stun_chance = random.random()  # 40% chance of spawning a stun effect
        return {'damage': base_damage, 'spawn_stun': spawn_stun_chance < 0.4}

    @staticmethod
    def x_bow_logic():
        base_damage = random.randint(60, 80)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}

    @staticmethod
    def goblin_hut_logic():
        spawn_goblins_chance = random.random()  # 60% chance of spawning Goblins
        return {'spawn_goblins': spawn_goblins_chance < 0.6}

    @staticmethod
    def mortar_logic():
        base_damage = random.randint(30, 40)
        return {'damage': base_damage}

    @staticmethod
    def inferno_tower_logic():
        base_damage = random.randint(40, 60)
        charge_bonus = random.random()  # 20% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.2}

    @staticmethod
    def bomb_tower_logic():
        base_damage = random.randint(40, 50)
        splash_damage = random.randint(20, 30)
        return {'damage': base_damage, 'splash_damage': splash_damage}

    @staticmethod
    def barbarian_hut_logic():
        spawn_barbarians_chance = random.random()  # 50% chance of spawning Barbarians
        return {'spawn_barbarians': spawn_barbarians_chance < 0.5}

    @staticmethod
    def tesla_logic():
        base_damage = random.randint(25, 35)
        return {'damage': base_damage}

    @staticmethod
    def elixir_collector_logic():
        elixir_generated = random.randint(5, 10)
        return {'elixir_generated': elixir_generated}

    @staticmethod
    def x_bow_logic():
        base_damage = random.randint(60, 80)
        charge_bonus = random.random()  # 30% chance of charging bonus
        return {'damage': base_damage, 'charge_bonus': charge_bonus < 0.3}

    @staticmethod
    def tombstone_logic():
        spawn_skeletons_chance = random.random()  # 70% chance of spawning Skeletons
        return {'spawn_skeletons': spawn_skeletons_chance < 0.7}

    @staticmethod
    def furnace_logic():
        base_damage = random.randint(15, 25)
        spawn_fire_spirits_chance = random.random()  # 80% chance of spawning Fire Spirits
        return {'damage': base_damage, 'spawn_fire_spirits': spawn_fire_spirits_chance < 0.8}

    @staticmethod
    def goblin_cage_logic():
        base_damage = random.randint(15, 25)
        spawn_goblin_brawler_chance = random.random()  # 50% chance of spawning Goblin Brawler
        return {'damage': base_damage, 'spawn_goblin_brawler': spawn_goblin_brawler_chance < 0.5}
    
    @staticmethod
    def fireball_logic():
        base_damage = random.randint(100, 200)
        return {'damage': base_damage}

    @staticmethod
    def arrows_logic():
        base_damage = random.randint(50, 100)
        return {'damage': base_damage}

    @staticmethod
    def rage_logic():
        rage_duration = random.randint(5, 10)
        return {'rage_duration': rage_duration}

    @staticmethod
    def rocket_logic():
        base_damage = random.randint(200, 300)
        return {'damage': base_damage}

    @staticmethod
    def goblin_barrel_logic():
        spawn_goblins_chance = random.random()  # 80% chance of spawning Goblins
        return {'spawn_goblins': spawn_goblins_chance < 0.8}

    @staticmethod
    def freeze_logic():
        freeze_duration = random.randint(5, 10)
        return {'freeze_duration': freeze_duration}

    @staticmethod
    def mirror_logic():
        # Double the damage of the last spell played
        return {'mirror_damage_multiplier': 2}

    @staticmethod
    def lightning_logic():
        base_damage = random.randint(300, 400)
        return {'damage': base_damage}

    @staticmethod
    def zap_logic():
        base_damage = random.randint(50, 100)
        return {'damage': base_damage}

    @staticmethod
    def poison_logic():
        base_damage = random.randint(50, 100)
        poison_duration = random.randint(5, 10)
        return {'damage': base_damage, 'poison_duration': poison_duration}

    @staticmethod
    def graveyard_logic():
        spawn_skeletons_chance = random.random()  # 90% chance of spawning Skeletons
        return {'spawn_skeletons': spawn_skeletons_chance < 0.9}

    @staticmethod
    def the_log_logic():
        base_damage = random.randint(100, 150)
        knockback_distance = random.randint(2, 5)
        return {'damage': base_damage, 'knockback_distance': knockback_distance}

    @staticmethod
    def tornado_logic():
        base_damage = random.randint(50, 100)
        pull_strength = random.randint(2, 5)
        return {'damage': base_damage, 'pull_strength': pull_strength}

    @staticmethod
    def clone_logic():
        # Duplicate all friendly troops in the spell area
        return {'duplicate_troops': True}

    @staticmethod
    def earthquake_logic():
        base_damage = random.randint(100, 150)
        # Reduce buildings' hitpoints by a certain percentage
        building_damage_reduction = random.uniform(0.1, 0.3)
        return {'damage': base_damage, 'building_damage_reduction': building_damage_reduction}

    @staticmethod
    def barbarian_barrel_logic():
        base_damage = random.randint(100, 150)
        return {'damage': base_damage}

    @staticmethod
    def heal_spirit_logic():
        heal_amount = random.randint(50, 100)
        return {'heal_amount': heal_amount}

    @staticmethod
    def giant_snowball_logic():
        base_damage = random.randint(50, 100)
        # Reduce the target's attack and movement speed for a short duration
        slow_duration = random.randint(2, 5)
        return {'damage': base_damage, 'slow_duration': slow_duration}

    @staticmethod
    def royal_delivery_logic():
        base_damage = random.randint(150, 200)
        return {'damage': base_damage}