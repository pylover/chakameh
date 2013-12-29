
import _id3reader

class MP3Reader(_id3reader.Reader):
    def __init__(self,f):
        _id3reader.Reader.__init__(self, f)
    
    @property
    def title(self):
        return self.getValue('title')
    
    @property
    def album(self):
        return self.getValue('album')

    @property
    def artist(self):
        return self.getValue('performer')

    @property
    def composer(self):
        return self.getValue('composer')
    
    @property
    def year(self):
        return self.getValue('year')
    
    @property
    def lyricist(self):
        return self.getValue('TEXT')
    
    @property
    def genere(self):
        return self.getValue('genere')
    
    @property
    def comment(self):
        return self.getValue('comment')    
    
#     def __repr__(self):
# #         if self.frames:
# #             return str(self.frames.keys())
# #         else:
# #             return '\n'
#         return u'%s\t%s\t%s\t%s\t%s\t%s\t%s' % (self.album,self.artist,self.composer,self.year,self.title,self.lyricist,self.genere)
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return u'%s\t%s\t%s\t%s\t%s\t%s\t%s' % (self.album,self.artist,self.composer,self.year,self.title,self.lyricist,self.genere)
