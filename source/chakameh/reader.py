import struct

def unsynchsafe(num):
    out = 0
    mask = 0x7f000000
    for i in range(4):
        out >>= 1
        out |= num & mask
        mask >>= 8
    return out

def synchsafe(num):
    mask = 0x0000007f
    ret = 0
    for i in range(4):
        t = num >> (i * 8)
        t &= mask
        t <<= (i * 8)
        ret |= t
        num <<= 1
    return ret

class BinaryReader(object):
    def __init__(self,fileobj):
        self.fileobj = fileobj
        self.size = 0
        
    def unpack(self,format,size,):
        self.size += size
        return struct.unpack(format,self.fileobj.read(size))
    
    def read_raw(self,size):
        self.size += size
        return self.fileobj.read(size)
    
class ID3V2(object):
    
    class Header(BinaryReader):
        def __init__(self,fileobj):
            BinaryReader.__init__(self, fileobj)
            self.version = self.unpack('!2B', 2)
            self.flags = self.unpack('!B',1)[0]
            self.size = unsynchsafe( self.unpack('!i',4)[0])

        @property
        def unsynchronisation(self):
            return bool(self.flags & 32)
          
        @property
        def has_extended_header(self):
            return bool(self.flags & 16)
        
        @property
        def experimental_indicator(self):
            return bool(self.flags & 8)
        
        @property
        def footer_present(self):
            return bool(self.flags & 4)

    class ExtendedHeader(BinaryReader):
        def __init__(self,fileobj):
            BinaryReader.__init__(self, fileobj)
            self.size = unsynchsafe( self.unpack('!i',4)[0])
            self.flagsize = self.unpack('!B',1)[0] 
            self.flags = self.read_raw(self.flagsize)

    class Frame(BinaryReader):
        def __init__(self,fileobj):
            BinaryReader.__init__(self, fileobj)
            self.id = self.unpack('!4s',4)[0]
            self.size = unsynchsafe( self.unpack('!i',4)[0])
            self.flags = self.read_raw(2)
            
            
    def read_frames(self,fileobj):
        
        
    
    def __init__(self,fileobj):
        self.header = ID3V2.Header(fileobj)
        if self.header.has_extended_header:
            self.extended_header = ID3V2.ExtendedHeader(fileobj)
        self.read_frames(fileobj)
        
        #print struct.unpack('!c', fileobj.read(1))
        #print fileobj.read(64)
    
    
    def __repr__(self):
        return "\n".join([ '%s:\t\t%s' % (k,_v) for k,_v in {
                 'Size'   : self.header.size,
                 'Flags'  : bin(self.header.flags),
                 'Ver': '.'.join([str(v) for v in self.header.version]),
                 'Footer': self.header.footer_present,
                 'ExHead': self.header.has_extended_header,
                 
                 }.items()])

class AudioFile(object):
    def __init__(self,filename):
        self.filename = filename
        print filename
        self._tags = {}
        self.parse()
    
    def parse(self):
        try:
            self.fileobj = open(self.filename,'rb')
            
            header = struct.unpack('!3s', self.fileobj.read(3))
            
            if len(header) and header[0] == 'ID3':
                self._tags['ID3V2'] = ID3V2(self.fileobj)
                print self._tags['ID3V2']
        finally:
            if self.fileobj:
                self.fileobj.close()
        

    def getValue(self,key):
        return '-----'
        
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

