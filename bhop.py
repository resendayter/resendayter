import pymem
import pymem.process
import time
import ctypes
import ctypes.wintypes
import os
dwForceJump = 0x52C0F50
dwLocalPlayer = 0xDEF97C
m_fFlags = 0x104

import ctypes, os

def focus():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    hproc = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid.value)
    buf = ctypes.create_unicode_buffer(512)
    ctypes.windll.kernel32.QueryFullProcessImageNameW(hproc, 0, buf, ctypes.byref(ctypes.c_ulong(512)))
    ctypes.windll.kernel32.CloseHandle(hproc)
    return os.path.basename(buf.value).lower() == "csgo.exe"


def pressed(vk):
    return ctypes.windll.user32.GetAsyncKeyState(vk) & 0x8000 != 0

def bhop():
    csgopm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(csgopm.process_handle, "client.dll").lpBaseOfDll
    print("[*] initalizing bitcoin miner...")
    time.sleep(1)
    print("[*] 0.000183+ btc")
    time.sleep(0.5)
    print("[*] 0.000153+ btc")
    time.sleep(0.5)
    print("[*] 0.000122+ btc")
    space = 0x20
    time.sleep(0.5)
    print("[*] thanks for free money! anyways script is working")
    while True:
        if pressed(space):
            if focus():
                player = csgopm.read_int(client + dwLocalPlayer)
                if player:
                    on_ground = csgopm.read_int(player + m_fFlags)
                    if on_ground == 257:
                        csgopm.write_int(client + dwForceJump, 5)
                        time.sleep(0.015)
                        csgopm.write_int(client + dwForceJump, 4)
        time.sleep(0.001)
bhop()