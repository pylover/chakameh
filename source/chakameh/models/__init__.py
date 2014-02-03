import os.path
from elixir import session
from elixir import metadata,setup_all
from elixir.options import options_defaults

# doing it right, before importing(defining) models
options_defaults['shortnames'] = True

from .artist import Artist
from .track import Track
from .lyricist import Lyricist
from .genere import Genere
from .composer import Composer
from .category import Category

thisdir = os.path.dirname(__file__)
metadata.bind = "sqlite:///%s" % os.path.abspath(os.path.join( thisdir, "../../.." ,"data/db.sqlite"))
metadata.bind.echo = False
setup_all(create_tables=True)        


__all__ = ['session',
           'metadata',
           'Artist',
           'Track',
           'Lyricist',
           'Category',
           'Genere',
           'Composer']
