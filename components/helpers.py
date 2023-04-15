import os
def check_directory(path):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                return False
            return True
        except FileExistsError:
            print("ERROR: Path already exists.")
        except FileNotFoundError:
            print("ERROR: Path not found.")
        except:
            print("ERROR: An error has occurred and the directory was not created nor found.")
        