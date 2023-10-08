import subprocess

def main():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        print(result)
        print("*" * 50)
        print(out)
        print("*" * 50)
        print(result.returncode)
        lst = "Ubuntu 22.04.1 LTS"
        lst2 = "Jammy Jellyfish"
        if lst in out and lst2 in out:
            print("SUCCESS")
        else:
            print("FAIL")


if __name__ == '__main__':
    main()