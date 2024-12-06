# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['profile_report.py'],
    pathex=[],
    binaries=[],
    datas=[('config', 'config'), ('D:/python/print_profile/logo.jpeg', '.'), ('D:/python/print_profile/chartmg.jpeg', '.'), ('D:/python/print_profile/channel.jpeg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='profile_report',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['FileIcon.ico'],
)
