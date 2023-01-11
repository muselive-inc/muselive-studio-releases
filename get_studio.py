import platform
import os


if __name__ == "__main__":
    mac_ver, _, chip  = platform.mac_ver()
    mac_ver = mac_ver.split('.')[0]
    os.system(f'curl https://studio.muse.live/0.11.0/museLIVEStudio_osx{mac_ver}_{chip}_v0.11.0.dmg -o studio.dmg')
    print("Download Complete")
