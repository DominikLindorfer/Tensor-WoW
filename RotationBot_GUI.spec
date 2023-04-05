# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Dominik/Programs/WoW-RotBot/RotationBot_GUI.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Dominik/Programs/WoW-RotBot/settings.json', '.'), ('C:/Users/Dominik/Programs/WoW-RotBot/themes', 'themes/'), ('C:/Users/Dominik/Programs/WoW-RotBot/WoWIcons', 'WoWIcons/'), ('C:/Users/Dominik/Programs/WoW-RotBot/saved_model_icons', 'saved_model_icons/'), ('C:/Users/Dominik/Programs/WoW-RotBot/Config', 'Config/'), ('C:/Users/Dominik/Programs/WoW-RotBot/Logo', 'Logo/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RotationBot_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Logo\\LogoV4_icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='RotationBot_GUI',
)
