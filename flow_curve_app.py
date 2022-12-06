#Signal path: Vaisala WMT700 --> RS232 --> Ardiuno --> TTY USB --> Host PC (Python)
#
#This script takes raw windspeed values and logs to file. Used for evaluating Vaisala WMt700
#KH 2017


import os
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from colorama import Fore
import os.path


def app_header():
    clear = lambda: os.system('cls')

    print(Fore.YELLOW, " _____ _                     ____                       ")
    print(Fore.YELLOW, "|  ___| | _____        __   / ___|   _ _ ____    _____   ")
    print(Fore.YELLOW, "| |_  | |/ _  \ \ / \ / /  | |  | | | | '__\ \ /  / _ \ ")
    print(Fore.YELLOW, "|  _| | | (_)  \  V  V /   | |__| |_| | |   \ V  /  __/ ")
    print(Fore.YELLOW, "|_|   |_|\___ / \_ /\_/     \____\__,_|_|    \_ / \___| ")
    print('')
    print(Fore.GREEN, '---------------------------------------------------------')

    for x in range(0, 30):
        print(Fore.CYAN, '\r' + '~~'*x, end='')
        time.sleep(.04)
        clear()
    print('')
    print(Fore.GREEN, '---------------------------------------------------------')

    return ()


def set_file():
    save_path = "C:\\Users\ka17360\\Desktop\\flow_curve"
    file_name = input('Enter file Name: ').strip() + '.csv'
    complete_name = os.path.join(save_path, file_name)
    return complete_name


def user_input(file_name, file_op):

    p = input("Enter Pressure(psi): ")
    t = input("Enter Time(s): ")
    m = input("Enter Mass(kg): ")
    if file_op is True:
        file = open(file_name, 'w')
    if file_op is False:
        file = open(file_name, 'a')
    file.write('\n')
    file.write(p)
    file.write(',')
    file.write(t)
    file.write(',')
    file.write(m)
    file.close()
    return ()


def curve_plot(f, p):
    style.use('seaborn')  # style
    plt.xlabel('Flow Rate (l/s)')  # x axis label
    plt.ylabel('Pressure (PSI)')  # y axis label
    plt.title("Quench Lab flow curve", fontsize=20)  # title
    plt.gcf().subplots_adjust(bottom=0.25)  # slightly resizes window
    plt.scatter(f, p)
    plt.show(block=False)
    plt.pause(2)
    plt.close()
    return ()


i = True  # flag to decided between read or append
app_header()
print(Fore.RED, '\n')
data_file = set_file()
while True:  # main event loop
    os.system("Color 9")
    user_input(data_file, i)
    df = pd.read_csv(data_file, header=None)
    df.columns = ['Pressure', 'Time', 'Mass']
    i = False
    pressure = df.loc[:, 'Pressure']
    time = df.loc[:, 'Time']
    mass = df.loc[:, 'Mass']
    flow = mass/time
    print(df)
    curve_plot(flow, pressure)

