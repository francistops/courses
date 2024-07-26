def meditate(mana, max_mana, energy, energy_potions):
    while mana != max_mana and (energy != 0 or energy_potions != 0):
        print('start loop', mana, max_mana, energy, energy_potions)
        energy -= 1
        mana += 3
        if mana > max_mana:
            print('power exeeded', mana)
            mana = max_mana
        if energy < 0:
            print('almost out of energy!', energy)
            if energy_potions >= 1:
                print('using potion!', energy_potions)
                energy_potions -= 1
                energy += 50

        print('end loop', mana, max_mana, energy, energy_potions, '\n')

    return mana, energy, energy_potions


print(meditate(1, 100, 33, 2))
print('answer: 100, 0, 2')
