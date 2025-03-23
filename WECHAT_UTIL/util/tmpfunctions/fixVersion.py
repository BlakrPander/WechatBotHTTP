import pymem


def getVersionNum(version):
    """
    将版本号转换为16进制
    :param version:
    :return:
    """
    verList = [hex(int(elem))[2:] for elem in version.split('.')]
    vNum = '0x6{}0{}0{}{}'.format(*verList)
    return int(vNum, 16)


def fixVersion(version):
    """
    修改微信版本号
    :param version:
    :return:
    """
    vNum = getVersionNum(version)
    p = pymem.Pymem()
    p.open_process_from_name("WeChat.exe")
    offsets = [0x2367624, 0x2385af0, 0x2385c44, 0x239c98c, 0x239eafc, 0x23a1604]
    # 获取 WeChatWin.dll 的基地址
    base_address = pymem.process.module_from_name(p.process_handle, "wechatwin.dll").lpBaseOfDll
    for offset in offsets:
        addr = base_address + offset
        p.write_int(addr, vNum)
    print("WeChat version now fixed to: {}".format(version))

if __name__ == '__main__':
    print("ok!")
    fixVersion('3.9.10.19')
