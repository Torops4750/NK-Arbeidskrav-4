import serial
import time
import sys

def main():

    while True:
        os = int(input("\nKva OS? 1 for linux, 2 for windows: "))
        if os == 1:
            comport="/dev/ttyS"
            break
        elif os == 2:
            comport = "COM"
            break
        else:
            print("Feil OS, prøv igjen")

    portnummer = input("\nKva portnummer: ")

    while True:
        device = int(input("\nKva device? 1 for router, 2 for switch: "))
        if device == 1:
            break
        elif device == 2:
            layer = int(input("Lag 2 eller 3? "))
            if layer == 2:
                break
            elif layer == 3:
                break
            else:
                print("Feil, prøv igjen: ")
        else:
            print("Prøv igjen: ")

    hostname = input("Hostname: ")
    hostname = "hostname " + hostname + "\r\n"
    domainname = input("Domain Name: ")
    domainname = "ip domain name " + domainname + "\r\n"
    username = input("Username: ")
    password = input("Password: ")
    user = "username " + username + " privilege 15 secret " + password  + "\r\n"
    vlanid = input("VLAN ID for management: ")
    sshsetup = "crypto key generate rsa modulus 2048\r\n"
    enablesecret = "enable secret " + password + "\r\n"

    if device == 1:
        interface = input("Interface: ")
        vlanint = ("int " + interface + "." + vlanid + "\r\nencapsulation dot1q " + vlanid + "\r\n")
        interfaceconf = "int " + interface + "\r\nno shut\r\nexit\r\n"
        ip = input("IP addresse til mgmt: ")
        subnettmask = input("Subnett maske: ")
        vlanip = "Ip address " + ip + " " + subnettmask + "\r\nno shut\r\nexit\r\n"

        # Try to establish console connection with the device.
        try:
            console = serial.Serial(
                port=comport+portnummer, # Change to your own COM port
                baudrate=9600,
                parity="N",
                stopbits=1,
                bytesize=8,
                timeout=8
            )

        # If there is an exception, print the error and exit the program.
        except serial.serialutil.SerialException as e:
            print('Error connecting to device...', e)
            sys.exit()

        # If there is no exception, run commands and print the output.
        else:
            console.write("\r\nno\r\nyes\r\n\r\n".encode())
            time.sleep(20)
            console.write("\r\nen\r\nconf t\r\n".encode())
            console.write(hostname.encode())
            console.write(domainname.encode())
            console.write(user.encode())
            console.write("crypto key generate rsa modulus 2048\r\n".encode())
            time.sleep(3)
            console.write("ip ssh version 2\r\nline vty 0 15\r\ntransport input ssh\r\nlogin local\r\nexit\r\n".encode())
            console.write(interfaceconf.encode())
            console.write(vlanint.encode())
            console.write(vlanip.encode())
            console.write(enablesecret.encode())
            console.write("do write\r\n".encode())
            time.sleep(.5)
            console.write("end\r\n".encode())

            output = console.read(4096).decode('utf-8')
            print(output)
    elif device == 2:
            
            vlan = "vlan " + vlanid + "\r\nname mgmt\r\nexit\r\n"
            vlanint = "int vlan " + vlanid + "\r\n\r\n"
            ip = input("IP address & maske: ")
            ip = "Ip address " + ip + "\r\nno shut\r\nexit\r\n"
            vlanswitchport = input("Kva switchport til VLAN? ")
            vlanswitchport = "int " + vlanswitchport + "\r\nswitchport access vlan " + vlanid + "\r\nexit\r\n"
            gateway = input("Default gateway: ")
            gateway = "ip default-gateway " + gateway + "\r\n"
            if layer == 2:

                # Try to establish console connection with the device.
                try:
                    console = serial.Serial(
                        port=comport + portnummer, # Change to your own COM port
                        baudrate=9600,
                        parity="N",
                        stopbits=1,
                        bytesize=8,
                        timeout=8
                    )

                # If there is an exception, print the error and exit the program.
                except serial.serialutil.SerialException as e:
                    print('Error connecting to device...', e)
                    sys.exit()

                # If there is no exception, run commands and print the output.
                else:
                    console.write("\r\nno\r\nyes\r\n".encode())
                    time.sleep(15)
                    console.write("\r\nen\r\nconf t\r\n".encode())
                    console.write(hostname.encode())
                    console.write(domainname.encode())
                    console.write(user.encode())
                    console.write("crypto key generate rsa modulus 2048\r\n".encode())
                    time.sleep(10)
                    console.write("ip ssh version 2\r\nline vty 0 15\r\n transport input ssh\r\n login local\r\n exit\r\n".encode())
                    console.write(vlan.encode())
                    console.write(vlanint.encode())
                    console.write(ip.encode())
                    console.write(gateway.encode())
                    console.write(vlanswitchport.encode())
                    console.write(enablesecret.encode())
                    console.write("do write\r\n".encode())
                    time.sleep(5)
                    console.write("end\r\n".encode())

                    output = console.read(4096).decode('utf-8')
                    print(output)
            elif layer == 3:

                # Try to establish console connection with the device.
                try:
                    console = serial.Serial(
                        port=comport + portnummer, # Change to your own COM port
                        baudrate=9600,
                        parity="N",
                        stopbits=1,
                        bytesize=8,
                        timeout=8
                    )

                # If there is an exception, print the error and exit the program.
                except serial.serialutil.SerialException as e:
                    print('Error connecting to device...', e)
                    sys.exit()

                # If there is no exception, run commands and print the output.
                else:
                    console.write("\r\nno\r\nyes\r\n".encode())
                    time.sleep(15)
                    console.write("\r\nen\r\nconf t\r\n".encode())
                    console.write(hostname.encode())
                    console.write(domainname.encode())
                    console.write(user.encode())
                    console.write("crypto key generate rsa modulus 2048\r\n".encode())
                    time.sleep(10)
                    console.write("ip ssh version 2\r\nline vty 0 15\r\ntransport input ssh\r\nlogin local\r\nexit\r\n".encode())
                    console.write(vlan.encode())
                    console.write(vlanint.encode())
                    console.write(ip.encode())
                    console.write(gateway.encode())
                    console.write(vlanswitchport.encode()) 
                    console.write(enablesecret.encode())
                    console.write("do write\r\n".encode())
                    time.sleep(5)
                    console.write("end".encode())
                    output = console.read(4096).decode('utf-8')
                    print(output)
                

if __name__ == "__main__":
    main()
