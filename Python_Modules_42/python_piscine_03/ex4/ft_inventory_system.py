#!/usr/bin/env python3

def ft_inventory_system():

    """
    This program generates, compares and modify inventories from players

    Variables:
        -items : dictionary with a nested dictionary that has all the
        information of the items we are going to use in the exercice
        -inventories : dicitionary with the players as key that has nested
        a new dictionary with the quantity of the objects the players have
    Funtionality:
        -Is just a hub with the information to send to the other funtions.
    Return:
        -This function doesn't return anything
    """

    def print_inventory(player, inventory, catalog):

        """
        This function Prints the inventory of the selected character in the
        state it is at the moment.

        Variables:
            -total_value : keeps the sum of the total value of each ot the
            items in the inventory
            -item_count : keeps the total count of all the items in the
            inventory
            -all_cat : is a dictionary that keeps the count of the categories
            from each item in the inventory
            -cat : looks for the category of item in the inventory and is used
            to index it to all_cat
        Functionality:
            -We looks for the items and his quantity in the selected player
             inventory.
            -we check and save variables that are required to be printed in
            in the exercice
            -we save the quiantity of each item in a new dictionary to print
            the name and the total quantity it has
        Return:
            -This function doesn't return anything
        """

        print("=== Print Inventory System ===")

        print(f"=== {player}'s Inventory ===")

        total_value = 0
        item_count = 0
        all_cat = dict({})

        for item, qnt in inventory.items():
            data = catalog.get(item)
            value = data.get('value') * qnt
            total_value += value
            item_count += qnt

            cat = data.get('type')
            all_cat[cat] = all_cat.get(cat, 0) + qnt

            print(f"{item} ({data.get('type')}, {data.get('rarity')} "
                  f"{qnt} x @ {data.get('value')}= {data.get('value') * qnt}")

        print(f"Inventory value: {total_value} gold")
        print(f"Item count: {item_count} items")
        print("Categories:", end=" ")
        for cat, count in inventory.items():
            print(f"{cat}({count})", end=" ")
        print("\n")

    def transaction(inventories, giver, reciever, item, quantity):

        """
        This funtion simulates a transaction between 2 players.

        Variables:
            -giver_inventory: takes the information from the inventory of
            giver
            -reciever inventory: takes the informatiion from the iventory of
            reciever
        Functionality:
            -we check if the character are indeed in the inventory dictionary
            -we check if the item required is in the giver inventory
            -we check if there are enough of the requireditems to transfer
            from giver
            -if there are, we take out the quantity of items required from
            giver and adds it to the reciever inventory. It automatically
            creates the entry if there is not entry in the reciever inventory
            -if there is 0 quantity of the traded item in the giver inventory
            it deletes the entry from the dictionary.
        Return:
            -This function doesn't return anything, just use it to break the
            operation
        """

        print(f"=== Transaction: {giver} "
              f"gives {reciever} {quantity} {item} ===")

        if giver not in inventories or reciever not in inventories:
            print(f"Invalid Player: {giver}")
            return

        giver_inv = inventories.get(giver)
        reciever_inv = inventories.get(reciever)

        if item not in giver_inv:
            print(f"Item not found: {item}")
            return

        if giver_inv.get(item) < quantity:
            print("Not enough items to transfer")
            return

        giver_inv[item] -= quantity
        reciever_inv[item] = reciever_inv.get(item, 0) + quantity

        print("Transaction successful!\n")

        print("=== Updated Inventories ===")
        print(f"{giver} {item}s: {giver_inv[item]}")
        print(f"{reciever} {item}s: {reciever_inv[item]}")

        if giver_inv[item] == 0:
            del giver_inv[item]

    def inventory_analitycs(inventories, items):

        """
        Ths function analices the inventory data provided from the main
        program

        Variables:
            -most_val_player :saves the most valuable player from both
            inventories
            -most_val : saves highest value between both inventores
            -most_items_player : saves the player with more items
            -most_items : saves the maximun quantitu of items in both
            inventories
            -rarest_items : saves the items with the "rarity" key : 'rare'
        Functionality:
            -check for each player in inventories each item it has.
            -saves and compare the information from one inventory to the
            another
            -finally prints all the information from the higest value inventory
        Return:
            -This function doesn't return anything.
        """

        most_val_player = None
        most_val = 0
        most_items_player = None
        most_items = 0
        rarest_items = []

        for player in inventories:
            total_value = 0
            item_count = 0
            for item, qnt in inventories[player].items():
                total_value += items[item].get('value') * qnt
                item_count += qnt
                info_item = items[item].get('rarity')

                if info_item == 'rare' and item is not rarest_items:
                    rarest_items = rarest_items + [item]

            if total_value > most_val:
                most_val = total_value
                most_val_player = player

            if item_count > most_items:
                most_items = item_count
                most_items_player = player

        print("=== Inventory Analitycs ===")
        print(f"Most valuable player: {most_val_player} ({most_val} gold)")
        print(f"Most items: {most_items_player} ({most_items} items)")
        print("Rarest items:", ", ".join(rarest_items))

    items = dict({
                "sword": dict({"type": "weapon",
                               "rarity": "rare",
                               "value": 500
                               }),

                "potion": dict({"type": "consumable",
                                "rarity": "common",
                                "value": 50
                                }),

                "shield": dict({"type": "armor",
                                "rarity": "uncommon",
                                "value": 200
                                }),

                "magic_ring": dict({"type": "vanity",
                                    "rarity": "rare",
                                    "value": 500
                                    })
    })

    inventories = dict({
                    "Alice": dict({
                                "sword": 1,
                                "potion": 5,
                                "shield": 1
                                }),

                    "Bob": dict({
                                "magic_ring": 1
                                })
    })

    print_inventory("Alice", inventories.get('Alice'), items)
    transaction(inventories, "Alice", "Bob", "potion", 2)
    inventory_analitycs(inventories, items)


if __name__ == "__main__":

    ft_inventory_system()
