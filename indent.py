class Monitor:
    def __init__(self, name):
        self.name = name


    def method_a(self):
        pass


    def method_b(self):
        pass


    def method_c(self):
        pass


class MonitorCat(Monitor):
    def method_a(self):
        print('MonitorCat named {} says a'.format(self.name))


    def method_b(self):
        print('MonitorCat named {} says b'.format(self.name))


    def method_c(self):
        print('MonitorCat named {} says c'.format(self.name))


class MonitorDog(Monitor):
    def method_a(self):
        print('MonitorDog named {} says a'.format(self.name))


    def method_b(self):
        print('MonitorDog named {} says b'.format(self.name))


    def method_c(self):
        print('MonitorDog named {} says c'.format(self.name))


def main():
    monitors = [MonitorCat('Garfield'), MonitorDog('Goofy')]
    for mon in monitors:
        mon.method_a()
        mon.method_b()
        mon.method_c()

if __name__ == '__main__':
    main()
