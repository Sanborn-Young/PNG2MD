# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['PNG2MD.py'],
    pathex=['C:\\Users\\theol\\python\\PNG2MD'],
    binaries=[],
    datas=[],
    hiddenimports=collect_submodules('cffi'),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PNG2MD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,  # Enable strip to remove debug symbols
    upx=True,  # Enable UPX compression
    upx_exclude=[],  # Leave this list empty to include all files in UPX compression
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,  # Ensure to strip in the COLLECT step as well
    upx=True,  # Ensure UPX compression in the COLLECT step as well
    upx_exclude=[],
    name='PNG2MD',
)
