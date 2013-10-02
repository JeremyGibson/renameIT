__author__ = 'jgibson'
##
## This software was developed at the State Records Center of the North Carolina Department of Cultural Resources
## Division of Archives and Records. It is intended as a utility to assist employees of state and local government
## in North Carolina who wish to apply file naming best practices to existing file structures.
##
## *****************************************WARNING ********************************************
## ** Renaming files can cause problems especially if the files being renamed are located on  **
## ** an Intranet, Shared Drive, or an Internet accessible drive. Before attempting to rename **
## ** make sure that you have tested this program on a set of test files, or you consult with **
## ** an IT specialist within your office or agency.                                          **
## *********************************************************************************************

import os
import time
import re


def rename_file(mpath, mfile):
    """Rename a file

        Keyword arguments:
        mpath -- The directory the current file resides.
        mfile -- The file to be renamed

    """
    original_path = mpath + "\\" + mfile
    iso_c_time = time.strftime("%Y_%m_%d", time.gmtime(os.path.getctime(original_path)))
    name_array = os.path.splitext(mfile)
    fname = name_array[0]
    fname = fname.replace('.', '_')
    fname = re.sub(r"[^\w\s]", '', fname)
    fname = fname.replace(' ', '_')
    fname = fname + "_" + iso_c_time
    final_path = mpath + "\\" + fname + name_array[1]

    #Let the user choose if whether or not to accept the normalized file name
    print "Would you like to replace \n" + original_path + " \n with \n" + final_path
    print "\n"
    resp = raw_input("Enter y or n: ")
    if resp == 'y':
        os.rename(original_path, final_path)
        print "Filename changed.\n"
        return

    #User did not want to use the default file name so let's see if they want to supply one

    #Let the user add some semantic information to the file name if they wish.
    print "Would you like to enter a custom file name for:\n " + original_path
    print "\n"
    resp = raw_input("Enter y or n: ")
    if resp == 'y':
        fname = raw_input("Enter the new file name without the extension: ")
        fname = fname + "_" + iso_c_time
        final_path = mpath + "\\" + fname + name_array[1]
        os.rename(original_path, final_path)
        print "Filename changed.\n"

    return


def get_root_path():
    """Prompt user for a directory structure to scan and rename files"""
    while True:
        var = raw_input("Enter the path containing files to be renamed (ex. C:\Documents): ")
        if os.path.exists(var):
            return var
        print "I can't find the path you requested. Can you try again?\n"


if __name__ == "__main__":
    print '''
    *****************************************WARNING ********************************************
    ** Renaming files can cause problems especially if the files being renamed are located on  **
    ** an Intranet, Shared Drive, or an Internet accessible drive. Before attempting to rename **
    ** make sure that you have tested this program on a set of test files, or you consult with **
    ** an IT specialist within your office or agency.                                          **
    *********************************************************************************************
    '''
    r_path = get_root_path()
    for root, dirs, files in os.walk(r_path):
        for f in files:
            rename_file(root, f)






