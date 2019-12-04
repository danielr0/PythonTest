
from shutil import copyfile
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#depends on your machine
root_dir = "/Users/danielr/@/Dev.NetCore/"

server_dir = root_dir + "/Server/Services/Siemplify.Server.Service/"
etl_dir = root_dir + "/Server/ETL/Siemplify.Server.ETL.DataProcessingEngine.Service/"

templates_dir = os.path.dirname(os.path.abspath(__file__)) + "/"
common_jname = "common.appsettings.json"
server_jname =  "server.appsettings.json"
etl_jname = "dataprocessing.appsettings.json"

class FileToReplace:
    name  = ""
    copy_from = ""
    copy_to = ""

    def __init__(self, file_name, template_path, destination_path):
        self.file_name = file_name
        self.copy_from = template_path + file_name
        self.copy_to = destination_path + file_name

        validate_path(self.copy_from)
        validate_path(self.copy_to)

    def copy(self):
        copyfile(self.copy_from, self.copy_to)
        print(bcolors.OKBLUE + "Copied: " + self.copy_from  + bcolors.ENDC + " to " + bcolors.OKBLUE + self.copy_to + bcolors.ENDC)

def validate_path(x):
    if not os.path.exists(x):
        raise Exception(bcolors.FAIL + "Error: " + x + " is not a valid file. Check file location, please"  + bcolors.ENDC)


def copy_files():

    files  = [FileToReplace(common_jname, templates_dir, server_dir),
              FileToReplace(server_jname, templates_dir, server_dir),
              FileToReplace(etl_jname, templates_dir, etl_dir)]

    for f in files:
        f.copy();

    print(bcolors.OKGREEN +  "Config files were copied." + bcolors.ENDC)


def main():
    print(bcolors.HEADER + "Going to replace server configuration files..." + bcolors.ENDC)
    copy_files()

if __name__ == "__main__":
    main()
