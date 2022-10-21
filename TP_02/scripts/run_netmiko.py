from traceback import print_tb
from netmiko import ConnectHandler
import json

def question_25(net_connect):
    pass


def question_26(net_connect):
    pass



def question_27(net_connect):
    pass


def question_28(net_connect):
    pass


def question_29(net_connect):
    pass


def question_30(net_connect):
    pass


def question_31(net_connect):
    pass


def question_32(net_connect):
    pass


def get_inventory():
    pass


def question_35():
    pass

def question_36():
    pass
      

if __name__ == "__main__":  
    print("** Begin **")

    r01 = {
    'device_type': 'cisco_ios',
    'host': '172.16.100.62',
    'username': 'cisco',
    'password': 'cisco'
    }  
    
    # net_connect = ConnectHandler(**r01)
    # print("** Content of net_connect **")
    # print(net_connect)

    # print("** Type of net_connect **")
    # print(type(net_connect))
    # ConnectHandler(show())
    # print("** End **")
   
   # Show command that we execute.
    command = "show ip int brief"
    #command = "show ip route"

    # with ConnectHandler(**r01) as net_connect:
    #     output = net_connect.send_command(command, use_textfsm=True)

    # Automatically cleans-up the output so that only the show output is returned
 
    # i = 0
    # while i < len(output): 
    #     InterfaceName = output[i]["intf"]
    #     command = "sh ip interface {}".format(InterfaceName)
        
    #     with ConnectHandler(**r01) as net_connect:
    #         InterfaceConfiguration = net_connect.send_command(command, use_textfsm=True)

    #     print('** Interface {} **'.format(InterfaceName))
    #     print(" ")
    #     print(InterfaceConfiguration)
    #     print(" ")
    #     print("** END Interface **")
    #     print(" ")

    #     i = i+1    

    command = "interface loopback1"
    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_config_set(command)
        #output += net_connect.save_config()
    
    print("")
    print(output)
    print("")
    
    print("** End **")
    pass