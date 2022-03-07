import time, threading, os, math, sys, pathlib
import subprocess, signal
import zipfile
import shutil
import configparser, getpass, socket
from pathlib import Path
from res.script.constant import AmlDebugConstant

RET_VAL_SUCCESS         = 0
RET_VAL_FAIL            = -1
RET_VAL_EXCEPTION       = -2



class AmlCommonUtils():
    AML_DEBUG_DIRECOTRY_DRIVE                   = 'NA'

    AML_DEBUG_MODULE_HOME                       = 0
    AML_DEBUG_MODULE_AUDIO                      = 1
    AML_DEBUG_MODULE_VIDEO                      = 2
    AML_DEBUG_MODULE_CEC                        = 3
    AML_DEBUG_MODULE_SYS_OPERATION              = 4
    AML_DEBUG_MODULE_BURN                       = 5
    AML_DEBUG_MODULE_MAX                        = AML_DEBUG_MODULE_BURN + 1

    AML_DEBUG_DIRECOTRY_ROOT_NAME               = "aml_debug"
    AML_DEBUG_TOOL_NAME_EXE                     = 'aml_debug_tool.exe'
    AML_DEBUG_PLATFORM_DIRECOTRY_LOGCAT         = '/data/logcat.txt'
    AML_DEBUG_PLATFORM_DIRECOTRY_DMESG          = '/data/dmesg.txt'
    AML_DEBUG_PLATFORM_DIRECOTRY_TOMBSTONE      = '/data/tombstones/' 
    AML_DEBUG_PLATFORM_DIRECOTRY_COMMON_INFO    = '/data/common_info.txt' 
    AML_DEBUG_TOOL_ICO_PATH                     = ':/debug.ico'
    AML_DEBUG_DIRECOTRY_CONFIG_NAME             = 'config.ini'
    moduleDirPathDict = {
        AML_DEBUG_MODULE_AUDIO    :   'audio',
        AML_DEBUG_MODULE_VIDEO    :   'video',
        AML_DEBUG_MODULE_CEC      :   'cec',
    }

    AML_DEBUG_TOOL_EXE_SERVER_PATH              = '\\\\10.28.49.68\\amlogic debug tool\\'
    AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME        = 'online_updater.exe'
    AML_DEBUG_TOOL_EXE_VERSION_FILE_NAME        = 'aml_debug_tool_version.ini'

    AML_DEBUG_LOG_LEVEL_V                       = 'V'
    AML_DEBUG_LOG_LEVEL_D                       = 'D'
    AML_DEBUG_LOG_LEVEL_I                       = 'I'
    AML_DEBUG_LOG_LEVEL_W                       = 'W'
    AML_DEBUG_LOG_LEVEL_E                       = 'E'
    AML_DEBUG_LOG_LEVEL_F                       = 'F'

    log_func = print   
    adb_cur_dev = ''

    def init():
        if Path("d:").exists():
            AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE = 'd'
        if AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE == 'NA' and Path("e:").exists():
            AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE = 'e'
        if AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE == 'NA' and Path("c:").exists():
            AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE = 'c'
        if AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE == 'NA':
            print('init: C, D, E drive not exist.')
            return -1

        if not Path(AmlCommonUtils.get_cur_root_path()).exists():
            print(AmlCommonUtils.get_cur_root_path() + " folder does not exist, create it.")
            os.makedirs(AmlCommonUtils.get_cur_root_path(), 777)
        if Path(AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME).exists():
            os.remove(AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME)
        return 0

    def get_cur_root_path():
        return AmlCommonUtils.AML_DEBUG_DIRECOTRY_DRIVE + ":\\" + AmlCommonUtils. AML_DEBUG_DIRECOTRY_ROOT_NAME
    def get_cur_root_ini_file_path():
        return AmlCommonUtils.get_cur_root_path() + "\\" + AmlCommonUtils. AML_DEBUG_DIRECOTRY_CONFIG_NAME

    def log(info, level='D'):
        if AmlCommonUtils.log_func == print:
            AmlCommonUtils.log_func(level + ' ' + info)
        else:
            AmlCommonUtils.log_func(info, level)

    def default_log(info, level):
        print(level + ' ' + info)

    def set_log_fuc(func):
        AmlCommonUtils.log_func = func
    def set_adb_cur_device(dev):
        AmlCommonUtils.adb_cur_dev = dev

    def pre_create_directory(createByModule, moduleEnableArray=0):
        if not Path(AmlCommonUtils.get_cur_root_path()).exists():
            AmlCommonUtils.log(AmlCommonUtils.get_cur_root_path() + " folder does not exist, create it.", AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)
            os.makedirs(AmlCommonUtils.get_cur_root_path(), 777)
        curTime = time.strftime("%Y%m%d_%H-%M-%S", time.localtime())
        curPullPcTimePath = AmlCommonUtils.get_cur_root_path() + "\\" + curTime
        AmlCommonUtils.log('pre_create_directory Current date:' + \
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ', directory is: ' + curPullPcTimePath, AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)
        os.makedirs(curPullPcTimePath, 777)
        modulePath = curPullPcTimePath
        if createByModule == AmlCommonUtils.AML_DEBUG_MODULE_HOME:
            if moduleEnableArray == 0:
                AmlCommonUtils.log('__pre_create_directory: cfg is null', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_E)
            for index in range(AmlCommonUtils.AML_DEBUG_MODULE_AUDIO, AmlCommonUtils.AML_DEBUG_MODULE_MAX):
                if moduleEnableArray[index] == True:
                        modulePath = curPullPcTimePath + "\\" + AmlCommonUtils.moduleDirPathDict[index]
                        os.makedirs(modulePath, 777)
        else:
            if createByModule in AmlCommonUtils.moduleDirPathDict:
                modulePath = curPullPcTimePath + "\\" + AmlCommonUtils.moduleDirPathDict[createByModule]
                os.makedirs(modulePath, 777)
                AmlCommonUtils.log('pre_create_directory create:' + modulePath)
            else:
                AmlCommonUtils.log('__pre_create_directory: createByModule:' + createByModule + ' invalid.', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_E)
        return curTime

    def get_current_time():
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%H:%M:%S", local_time)
        decimals_t, integers_t =math.modf(ct)
        data_secs = (ct - integers_t) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        return time_stamp

    def get_path_by_module(time, id):
        return AmlCommonUtils.get_cur_root_path() + "\\" + time +  "\\" + AmlCommonUtils.moduleDirPathDict[id]

    def logcat_start(callbackFinish='', delayEndS=-1):
        logcatProcThread = threading.Thread(target=AmlCommonUtils.__logcat_wait_thread, args=(callbackFinish, delayEndS,))
        logcatProcThread.setDaemon(True)
        logcatProcThread.start()

    def __logcat_wait_thread(callbackFinish, delayEndS):
        AmlCommonUtils.log('__logcat_wait_thread: time:' + str(delayEndS) + 's, logcat loading...', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)
        logcatProcThread = threading.Thread(target=AmlCommonUtils.__logcat_run_thread)
        logcatProcThread.setDaemon(True)
        logcatProcThread.start()
        if delayEndS != -1:
            time.sleep(delayEndS)
            AmlCommonUtils.logcat_stop()
            callbackFinish()

    def __logcat_run_thread():
        AmlCommonUtils.log('__logcat_run_thread: Start logcat+++++')
        AmlCommonUtils.exe_adb_shell_cmd('logcat -G 40M;logcat -c;logcat > ' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_LOGCAT, True)
        AmlCommonUtils.log('__logcat_run_thread: Exit logcat------')

    def logcat_stop():
        AmlCommonUtils.exe_adb_shell_cmd('ps -ef |grep -v grep|grep logcat| awk \'{print $2}\'|xargs kill -9', True)

    def pull_logcat_to_pc(pc_path):
        AmlCommonUtils.exe_adb_cmd('pull "' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_LOGCAT + '" ' + pc_path, True)

    def pull_tombstones_to_pc(pc_path):
        AmlCommonUtils.exe_adb_cmd('pull "' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_TOMBSTONE + '" ' + pc_path, True)

    def pull_common_info_to_pc(pc_path):
        AmlCommonUtils.exe_adb_cmd('pull "' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_COMMON_INFO + '" ' + pc_path, True)

    def cap_common_debug_info(pc_path):
        AmlCommonUtils.exe_adb_shell_cmd('echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ >> "' 
            + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_COMMON_INFO)
        AmlCommonUtils.exe_adb_shell_cmd('date >> "' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_COMMON_INFO)
        AmlCommonUtils.exe_adb_shell_cmd('ps -ef >> "' + AmlCommonUtils.AML_DEBUG_PLATFORM_DIRECOTRY_COMMON_INFO)

    def bugreport(path):
        AmlCommonUtils.log('Start bugreport+++++', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)
        AmlCommonUtils.exe_adb_cmd('bugreport ' + path, True)
        AmlCommonUtils.log('Exit bugreport-----', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)

    def dmesg():
        AmlCommonUtils.log('dmesg', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_I)
        AmlCommonUtils.exe_adb_shell_cmd('rm ' + ' /data/dmesg.txt -rf', True)
        AmlCommonUtils.exe_adb_shell_cmd('dmesg' + ' > /data/dmesg.txt', True)

    def adb_root():
        return AmlCommonUtils.exe_adb_cmd('root', True)

    def adb_remount():
        return AmlCommonUtils.exe_adb_cmd('remount', True)

    def adb_reboot():
        return AmlCommonUtils.exe_adb_cmd('reboot', True)

    def adb_connect_by_ip(ip):
        connect_ip_cmd = 'adb connect ' + ip
        ret = AmlCommonUtils.exe_sys_cmd(connect_ip_cmd, True)
        if 'connected to ' + ip not in ret:
            AmlCommonUtils.log('adb connect ip:' + ip + ' failed !!!', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_E)
            return ''
        dev_name = ''
        dev_list = AmlCommonUtils.get_adb_devices()
        for dev in dev_list:
            if ip in dev:
                dev_name = dev
                break
        if dev_name == '':
            AmlCommonUtils.log('adb_connect_by_ip can\'t find ip:' + ip + ' in the listView.', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_E)
            return  ''
        AmlCommonUtils.set_adb_cur_device(dev_name)
        AmlCommonUtils.adb_root()
        AmlCommonUtils.exe_sys_cmd(connect_ip_cmd, True)
        AmlCommonUtils.adb_remount()
        return dev_name

    def exe_adb_shell_getprop_cmd(cmd, bprint=False):
        return AmlCommonUtils.exe_adb_cmd('shell getprop "' + cmd + '"', bprint)

    def exe_adb_shell_cmd(cmd, bprint=False):
        return AmlCommonUtils.exe_adb_cmd('shell "' + cmd + '"', bprint)

    def exe_adb_cmd(cmd, bprint=False):
        if AmlCommonUtils.adb_cur_dev != '':
            return AmlCommonUtils.exe_sys_cmd('adb -s ' + AmlCommonUtils.adb_cur_dev + ' ' + cmd , bprint)
        else:
            return AmlCommonUtils.exe_sys_cmd('adb ' + cmd , bprint)

    class ForceStop:
        def __init__(self):
            self.stop = False

    def exe_sys_cmd(cmd, bprint=False, path=None, forceStop=None):
        try:
            ret = ''
            proc = subprocess.Popen(cmd, shell=True, start_new_session=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, cwd=path)
            proc.stdin.close()
            for line in iter(proc.stdout.readline, b''):
                temp_str = line.strip().decode('utf-8')
                if temp_str != '\n' and temp_str != '':
                    ret = ret + temp_str + '\n'
                if bprint:
                    AmlCommonUtils.log(temp_str, AmlCommonUtils.AML_DEBUG_LOG_LEVEL_V)
                if forceStop != None and forceStop.stop == True:
                    proc.kill()
                    proc.terminate()
                    os.killpg(proc.pid, signal.SIGTERM)
            proc.wait()
            proc.stdout.close()
            if proc.returncode != RET_VAL_SUCCESS:
                AmlCommonUtils.log(cmd + ' --> Failed' + ', ret:'+ str(proc.returncode), AmlCommonUtils.AML_DEBUG_LOG_LEVEL_F)
            return ret
        except:
            AmlCommonUtils.log('exe_sys_cmd:' + cmd + ' --> Exception happend!!!', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_F)
            return ''

    def get_adb_devices():
        devs_list = []
        ret = AmlCommonUtils.exe_sys_cmd('adb devices', True)
        i = 0
        devs = ret.split('\n')
        for dev in devs:
            dev.replace('\n', '')
            # The i=0 first line is not adb device id.
            if i > 0 and dev != '':
                id = dev.split()[0]
                if id != '*':
                    devs_list.append(id)
                # print('id:' + id)
            i += 1
        return devs_list

    @staticmethod
    def zip_compress(srcPathName, targetPathName):
        z = zipfile.ZipFile(targetPathName,'w',zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(srcPathName):
            fpath = dirpath.replace(srcPathName,'')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename),fpath+filename)
        z.close()

    # 删除指定目录下的所有文件以及文件夹
    @staticmethod
    def del_all_file_and_direcotry(filepath):
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    @staticmethod
    def del_spec_file(filePath):
        if os.path.exists(filePath):
            try:
                os.remove(filePath)
            except:
                AmlCommonUtils.log('del_spec_file delete file:' + filePath + ' failed.', AmlCommonUtils.AML_DEBUG_LOG_LEVEL_F)

    def generate_snapshot(path):
        ini = configparser.ConfigParser()

        section = 'Amlogic_debug_tool_snapshot'
        ini.add_section(section)
        ini.set(section, 'version', AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_VERSION + ' (' + AmlDebugConstant.AML_DEBUG_TOOL_COMPILE_EXE_TYPE + ')')
        ini.set(section, 'compile_user', AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_USERE)
        ini.set(section, 'compile_time', AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_DATE)
        ini.set(section, 'commit_hash', AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_COMMIT)

        section = 'PC_snapshot'
        ini.add_section(section)
        ini.set(section, 'cur_debug_user', getpass.getuser())
        ini.set(section, 'cur_debug_timezone', str(time.tzname))
        ini.set(section, 'cur_debug_time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        hostname = socket.gethostname()
        ini.set(section, 'cur_debug_host', hostname)
        ini.set(section, 'cur_debug_ip', socket.gethostbyname(hostname))

        section = 'debug_platform_snapshot'
        ini.add_section(section)
        ini.set(section, 'soc_product', AmlCommonUtils.exe_adb_shell_getprop_cmd('ro.build.product').replace('\n', ''))
        ini.set(section, 'build_date', AmlCommonUtils.exe_adb_shell_getprop_cmd('ro.build.date').replace('\n', ''))
        ini.set(section, 'android_api', AmlCommonUtils.exe_adb_shell_getprop_cmd('ro.build.version.sdk').replace('\n', ''))
        ini.set(section, 'system_build_version', AmlCommonUtils.exe_adb_shell_getprop_cmd('ro.build.fingerprint').replace('\n', ''))
        ini.set(section, 'cur_platform_date', AmlCommonUtils.exe_adb_shell_cmd('date').replace('\n', ''))

        with open(path + '\\snapshot.ini', 'w+') as file:
            ini.write(file)

    def check_for_updates():
        upgrade_exe_file_path_server = AmlCommonUtils.AML_DEBUG_TOOL_EXE_SERVER_PATH + AmlCommonUtils.AML_DEBUG_TOOL_NAME_EXE
        upgrade_version_file_path_server = AmlCommonUtils.AML_DEBUG_TOOL_EXE_SERVER_PATH + AmlCommonUtils.AML_DEBUG_TOOL_EXE_VERSION_FILE_NAME
        upgrade_online_updater_file_path = AmlCommonUtils.AML_DEBUG_TOOL_EXE_SERVER_PATH + AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME
        try:
            if not Path(AmlCommonUtils.AML_DEBUG_TOOL_EXE_SERVER_PATH).exists():
                AmlCommonUtils.log('[check_for_updates] Connect server failed!')
                return -1, ''
            if not Path(upgrade_exe_file_path_server).exists():
                AmlCommonUtils.log('[check_for_updates] ' + AmlCommonUtils.AML_DEBUG_TOOL_NAME_EXE + ' not exists')
                return -1, ''
            if not Path(upgrade_version_file_path_server).exists():
                AmlCommonUtils.log('[check_for_updates] ' + AmlCommonUtils.AML_DEBUG_TOOL_EXE_VERSION_FILE_NAME + ' not exists')
                return -1, ''
            if not Path(upgrade_online_updater_file_path).exists():
                AmlCommonUtils.log('[check_for_updates] ' + AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME + ' not exists')
                return -1, ''
        except:
            AmlCommonUtils.log('[check_for_updates] An except occurs.')
            return -1, ''

        ini = configparser.ConfigParser()
        ini.read(upgrade_version_file_path_server)
        server_version = ini['AMLOGIC']['version']
        server_version_array = server_version.split('.')
        cur_version_array = AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_VERSION.split('.')
        if len(server_version_array) != len(cur_version_array):
            AmlCommonUtils.log('[check_for_updates] version invalid, cur:' + AmlDebugConstant.AML_DEBUG_TOOL_ABOUT_VERSION + ', server:' + server_version)
            return -1, ''
        for i, val in enumerate(server_version_array):
            # AmlCommonUtils.log('[check_for_updates] ' + 'i:' + str(i) + ',server:' + server_version_array[i] + ', cur:' + cur_version_array[i])
            if int(server_version_array[i]) > int(cur_version_array[i]):
                AmlCommonUtils.log('[check_for_updates] You can update the software to version:' + server_version)
                return 1, server_version
            elif int(server_version_array[i]) == int(cur_version_array[i]):
                continue
            else :
                break
        AmlCommonUtils.log('[check_for_updates] Your software is up to date!')
        return 0, ''

    def update_tool_now():
        upgrade_online_updater_file_path = AmlCommonUtils.AML_DEBUG_TOOL_EXE_SERVER_PATH + AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME
        try:
            os.system('copy "' + upgrade_online_updater_file_path +  '" .\\')
        except:
            AmlCommonUtils.log('[update_tool_now] An except occurs.')
        proc = subprocess.Popen(AmlCommonUtils.AML_DEBUG_TOOL_EXE_OTA_EXE_FILE_NAME + ' ' + AmlDebugConstant.AML_DEBUG_TOOL_COMPILE_EXE_TYPE, \
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        proc.stdin.close()
        proc.stdout.close()
        AmlCommonUtils.log('Upgrade is starting')
        sys.exit(0)
