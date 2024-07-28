# ef remove_duplicates(spells):
#   filtered_spells = []
#   uniq_spells = set()
#   for spell in spells:
#       uniq_spells.add(spell)
#       print(uniq_spells)
#   for uniq_spell in uniq_spells:
#       filtered_spells.append(uniq_spell)

#   return filtered_spells


# ef remove_duplicates(spells):
#   filtered_spells = []
#   uniq_spells = set(spells)
#   for uniq_spell in uniq_spells:
#       filtered_spells.append(uniq_spell)

#   return filtered_spells


def remove_duplicates(spells):
    uniq_spells = set(spells)
    spells = list(uniq_spells)

    return spells
