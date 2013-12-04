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

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
'''
import os
import time
import re

BULK_BOOL = ""
PREPEND_BOOL = ""
PRE_STRING = ""
APPEND_STRING = ""
MENU_CHOICE = ""
ROOT_PATH = ""


def rename_file_manual(mpath, mfile):
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

    if MENU_CHOICE == "3":
        print "Normalizing " + original_path
        os.rename(original_path, final_path)
        print "Filename normalized.\n"
        return
    elif MENU_CHOICE == "4":
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

def rename_file_bulk(mpath, mfile, string):
    original_path = mpath + "\\" + mfile
    name_array = os.path.splitext(mfile)
    if MENU_CHOICE == "2":
        new_name = string + name_array[0]
    else:
        new_name = name_array[0] + string

    final_path = mpath + "\\" + new_name + name_array[1]
    os.rename(original_path, final_path)

def get_root_path():
    """Prompt user for a directory structure to scan and rename files"""
    global ROOT_PATH
    while True:
        var = raw_input("Enter the path containing files to be renamed (ex. C:\Documents): ")
        if os.path.exists(var):
            ROOT_PATH = var
            return
        print "I can't find the path you requested. Can you try again?\n"

def menu():
    global MENU_CHOICE
    print '''
    ( 1 ) Bulk Rename - Append
    ( 2 ) Bulk Rename - Prepend
    ( 3 ) Normalize Files - Bulk
    ( 4 ) Normalize Files - Manual
    ( 5 ) Exit

    '''
    MENU_CHOICE = raw_input("Which rename do you want to do? ")

def set_options():
    global PREPEND_BOOL
    global PRE_STRING
    global APPEND_STRING

    str = raw_input("Enter the filename addition: ")
    if MENU_CHOICE == "1":
        APPEND_STRING = str
    else:
        PRE_STRING = str

def walk():
        for root, dirs, files in os.walk(ROOT_PATH):
            for f in files:
                if MENU_CHOICE == "1":
                        rename_file_bulk(root, f, APPEND_STRING)
                        print "Filename(s) changed.\n"
                elif MENU_CHOICE == "2":
                        rename_file_bulk(root, f, PRE_STRING)
                elif MENU_CHOICE == "3" or MENU_CHOICE == "4":
                    rename_file_manual(root, f)


if __name__ == "__main__":
    print '''
    ********************************WARNING ******************************
    ** Renaming files can cause problems especially if the files being  **
    ** renamed are located on an Intranet, Shared Drive, or an Internet **
    ** accessible drive. Before attempting to rename make sure that you **
    ** have tested this program on a set of test files, or you consult  **
    ** with an IT specialist within your office or agency.              **
    **********************************************************************

    '''

    while True:
        menu()
        if MENU_CHOICE == "1" or MENU_CHOICE == "2":
            get_root_path()
            set_options()
            walk()
        elif MENU_CHOICE == "3" or MENU_CHOICE == "4":
            get_root_path()
            walk()
        elif MENU_CHOICE == "5":
            print "\n\nThanks for flying with the North Carolina State Archives\n"
            break