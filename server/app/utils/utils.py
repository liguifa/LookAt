class Utils:

    @classmethod
    def list_to_dict(cls, items, get_key):
        result = dict()
        for item in items:
            result[get_key(item)] = item
        return result
