import pony

from pony import orm as orm

db = orm.Database()

class Tag(db.Entity):
    value = orm.Required(str)
    as_tag = orm.Set('PDF', lazy=False, reverse='tags')
    as_subject = orm.Set('PDF', lazy=False, reverse='subjects')


    def remove(self):
        with orm.db_session:
            Tag[self.id].delete()


class PDF(db.Entity):
    address = orm.PrimaryKey(str)
    tags = orm.Set(Tag)
    subjects = orm.Set(Tag)
    is_eng = orm.Required(bool)


    def remove(self):
        with orm.db_session:
            PDF[self.address].delete()


db.bind('sqlite', 'pdf_manager.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


def add_tag(value):
    if value:
        Tag(value=value)
        orm.commit()


def add_PDF(address, tags, subjects, is_eng):
    PDF(address=address, tags=tags, subjects=subjects, is_eng=is_eng)
    orm.commit()


def all_PDFs():
    with orm.db_session:
        return orm.select(p for p in PDF)


def all_tags():
    with orm.db_session:
        return orm.select(t for t in Tag).order_by(Tag.value)




orm.show(PDF)
orm.show(Tag)