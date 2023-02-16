import os
import shutil


## Set of utils and help method

def copy_theme_to_device(result_xml):
    """
    Copy spcific file to the android device
    :param result_xml:
    """
    # copy xml theme file to android device
    os.popen(
        "adb push {} /sdcard/Android/data/menion.android.locus/files/Locus/mapsVector/_themes/lomaps_v4/{}"
        .format(result_xml, os.path.basename(result_xml)))

    # refresf theme for renderer
    os.popen(
        "adb shell am broadcast -p menion.android.locus -a com.asamm.locus.ACTION_TASK --es tasks '''{ map_reload_theme: {} }'''")


def delete_folder_content(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete {}}. Reason: {}}'.format(file_path, e))
