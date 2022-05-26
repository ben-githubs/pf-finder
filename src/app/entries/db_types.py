import sqlalchemy.types as types

class Bulk(types.TypeDecorator):
    """ Acts as an Integer, with a special value L equal to 1/10. """

    impl = types.Integer