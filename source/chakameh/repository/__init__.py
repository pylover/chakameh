
from elixir import session
from elixir.options import options_defaults
options_defaults['shortnames'] = True
from .artist import Artist
from .category import Category
from .track import Track
from .lyricist import Lyricist
from .genere import Genere
from .composer import Composer
import os.path
thisdir = os.path.dirname(__file__)
from elixir import metadata,setup_all,create_all

def init():
    metadata.bind = "sqlite:///%s" % os.path.abspath(os.path.join( thisdir, "../../.." ,"data/db.sqlite"))
    metadata.bind.echo = False
    setup_all()#create_tables=True)
    create_all()        

class Repository(object):
    def __init__(self):
        pass
    
    def add_artist(self,title):
        if not title or title.strip()=='':
            return None
        artist = Artist.query.filter(Artist.title == title).first()
        if not artist:
            artist = Artist(title = title)
            session.commit()
        return artist

    def add_category(self,title):
        if not title or title.strip()=='':
            return None
        cat = Category.query.filter(Category.title == title).first()
        if not cat:
            cat = Category(title = title)
            session.commit()
        return cat

    def add_lyricist(self,title):
        if not title or title.strip()=='':
            return None
        lyricist = Lyricist.query.filter(Lyricist.title == title).first()
        if not lyricist:
            lyricist = Lyricist(title = title)
            session.commit()
        return lyricist

    def add_genere(self,title):
        if not title or title.strip()=='':
            return None
        genere = Genere.query.filter(Genere.title == title).first()
        if not genere:
            genere = Genere(title = title)
            session.commit()
        return genere

    def add_composer(self,title):
        if not title or title.strip()=='':
            return None
        composer = Composer.query.filter(Composer.title == title).first()
        if not composer:
            composer = Composer(title = title)
            session.commit()
        return composer


    def add_track(self,code,prime,**kw):
        kw['code'] = code
        kw['prime'] = prime
        if 'title' not in kw:
            kw['title'] = prime
         
        track = Track.query.filter(Track.code == code).first()
        if not track:
            track = Track(**kw)
        else:
            track.from_dict(kw)
        
        return track 
        
    def commit(self):
        session.commit()
    
    
    
    def get_artists(self):
        pass
    
    def get_composers(self):
        pass
    
    def get_poet(self):
        pass
    
    def get_dastgahs(self):
        pass
    
    def add_filters(self,filters):
        pass

    def delete_filters(self,filters):
        pass

    def clear_filters(self):
        pass
    