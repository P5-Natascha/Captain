from sensors import battery_ampere

def main():
    print("===Testmode ===")
    chan0 = battery_ampere.initmcp()
    battery_ampere.readampere(chan0)




if __name__ == '__main__':
    main()
