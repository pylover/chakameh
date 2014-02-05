# -*- mode: python -*-

from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals(),hookspath=['D:\\Kivy-w32\\chakameh\\pyinstaller\\hooks'])

hiddenimports = []
#from PyInstaller.hooks.hookutils import collect_submodules
#hiddenimports += collect_submodules('sqlalchemy')
hiddenimports += ['elixir']
#hiddenimports += ['contextlib']
#hiddenimports += ['decimal','numbers','datetime']



a = Analysis(['../source/chakameh.py'],
             hiddenimports=hiddenimports,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
#		  [('v', None, 'OPTION'),('W ignore', None, 'OPTION')],
          exclude_binaries=True,
          name='chakameh.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
		  
coll = COLLECT(exe,
			   Tree('../source',excludes=['.*']),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='chakameh')
