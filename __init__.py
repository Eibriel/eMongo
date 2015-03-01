

class Connection():
    def register(self, documents):
        pass


class Document():
    _data = {}

    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        # print ("{0}: {1}({2})".format(key, value, type(value)))
        if not key in self.structure:
            raise ValueError("Out of structure")
        elif self.structure[key] != None and\
                not self.structure[key] == type(value):
            raise ValueError(
                "Incorrect type, expected {0}, given {1}".format(
                    self.structure[key], type(value)))
        elif not self.validators[key](value):
            raise ValueError("Validation Error")
        else:
            self._data[key] = value

    def safe(self):
        safe_data = {}
        for dkey in self._data:
            if self.structure[dkey] != None:
                safe_data[dkey] = self._data[dkey]
            else:
                safe_data[dkey] = self._data[dkey].safe()
        return safe_data

    # Validators
    def max_length(length):
        def validate(value):
            return len(value) <= length
        return validate

    def min_max_val(min_, max_):
        def validate(value):
            return value >= min_ and value <= max_
        return validate

    def min_val(min_):
        def validate(value):
            return value >= min_
        return validate

    def any_val():
        def validate(value):
            return True
        return validate

    def in_list(list_):
        def validate(value):
            return value in list_
        return validate

    def if_type_in(list_):
        def validate(value):
            return type(value) in list_
        return validate
