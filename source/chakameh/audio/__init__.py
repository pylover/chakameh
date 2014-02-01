
import platform

if platform.system().lower().startswith('win'):
    from .sound_win32 import Sound
else:
    from .sound_posix import Sound
    
