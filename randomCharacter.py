import json
import os
from random import choices, choice, shuffle


class character:

    def __init__(self, char_class):
        with open('classes/'+char_class +'.json', "r") as read_file:
            self.data = json.load(read_file)
            self.rand_class = self.data["className"]

    def set_stats(self):
        self.stat_name = ["str","dex","con","int","wis","cha"]
        shuffle(self.stat_name)
        self.rolled_stats = stat_gen()
        self.rolled_stats.sort(reverse=True)
        self.stat_order = self.data["special"]["bestStats"][choice(self.data["special"]["statOption"])]
        for s in self.stat_name:
            if s not in self.stat_order:
                self.stat_order.append(s)

        self.stat_order = dict(zip(self.stat_order, self.rolled_stats))
        print(self.data["className"])
        print(self.stat_order)

    def set_skills(self):
        self.skills_number = self.data["skillsNumber"]
        self.skill_list = self.data["skills"]
        shuffle(self.skill_list)
        self.skills = []
        while self.skills_number > 0:
            self.skills.append(self.skill_list.pop())
            self.skills_number -= 1
        print(self.skills)

    def set_spells(self):
        self.cantrip_list = []
        with open('spells/cantrips.json', "r") as read_file:
            self.spells_data = json.load(read_file)

        for spell in self.spells_data:

            if self.rand_class in self.spells_data[spell]["class"]:
                self.cantrip_list.append(spell)

        shuffle(self.cantrip_list)
        self.cantrips = []
        self.cantrip_number = 0
        try:
            self.cantrip_number = self.data["special"]["spellsCantrip"]
        except KeyError:
            pass
        while self.cantrip_number > 0:
            self.cantrips.append(self.cantrip_list.pop())
            self.cantrip_number -= 1
        print(self.cantrips)

        self.spell_1_list = []
        with open('spells/first_level.json', "r") as read_file:
            self.spells_data = json.load(read_file)

        for spell in self.spells_data:

            if self.rand_class in self.spells_data[spell]["class"]:
                self.spell_1_list.append(spell)

        shuffle(self.spell_1_list)
        self.level_1 = []
        self.level_1_number = 0
        try:
            self.level_1_number = self.data["special"]["spellsLvlOne"]
        except KeyError:
            pass
        while self.level_1_number > 0:
            self.level_1.append(self.spell_1_list.pop())
            self.level_1_number -= 1
        print(self.level_1)








def stat_gen():
    statReturn = []
    for i in range(6):
        statReturn.append(choices(
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [0.1, 0.3, 0.8, 1.6, 2.9, 4.8, 7, 9.4, 11.4, 12.9, 13.3, 12.3, 10.1, 7.3, 4.2, 1.6],
        k=1)[0]
        )
    return statReturn

def class_choice():
    file = choice(['fighter', 'wizard', 'barbarian', 'bard', 'cleric', 'druid', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock'])
    return file

rand_char = character(class_choice())
rand_char.set_stats()
rand_char.set_skills()
rand_char.set_spells()
