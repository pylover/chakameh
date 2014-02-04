# -*- mode: python -*-

from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())

a = Analysis(['../source/chakameh.py'],
             hiddenimports=[
						'kivy.uix.selectableview',
						'elixir',
						'sqlalchemy.sql',
						'sqlalchemy'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
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
