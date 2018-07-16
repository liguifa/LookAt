from ..utils import Utils


class Menu:
    def __init__(self):
        self.id = 0
        self.display_name = ""
        self.url = ""
        self.sub_menus = []

    @classmethod
    def convert_to_menu(cls, entity_menus):
        menus = []
        all_ids = [entity_menu.id for entity_menu in entity_menus]
        top_level_ids = list(set([entity_menu.id for entity_menu in entity_menus if entity_menu.parent_id not in all_ids]))  # NOQA
        id_menu_map = Utils.list_to_dict(entity_menus, lambda m: m.id)
        print(len(top_level_ids))
        for top_level_id in top_level_ids:
            print(top_level_id)
            if top_level_id in id_menu_map.keys():
                print("add")
                entity_menu = id_menu_map.get(top_level_id)
                print(entity_menu)
                menu = Menu()
                menu.id = entity_menu.id
                menu.display_name = entity_menu.display_name
                menu.url = entity_menu.url
                print("append")
                for e_menu in entity_menus:
                    print("e_menu.parent_id:" + str(e_menu.parent_id))
                    print("menu.id:" + str(menu.id))
                    if e_menu.parent_id == menu.id:
                        sub_menu = Menu()
                        sub_menu.id = e_menu.id
                        sub_menu.display_name = e_menu.display_name
                        sub_menu.url = e_menu.url
                        menu.sub_menus.append(sub_menu)
                menus.append(menu)
        print(len(menus))
        return menus
