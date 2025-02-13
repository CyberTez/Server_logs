"""
Use this script to define your Domain class

Provide a '__main__' to test by creating a class, using at least
one member method, and printing to screen

"""

class Domain:
    def __init__(self,date, ip_addy, name_of_site, bytes):
        self.date = date
        self.ip_addy = ip_addy
        self.name_of_site = name_of_site
        self.bytes = bytes

        self.__date = str(date)
        self.__ip_addy = str(ip_addy)
        self.__name_of_site = str(name_of_site)
        self.__bytes = int(bytes)
    def __lt__(self, other):
        return self.name_of_site < other.name_of_site

    def __eq__(self, other):
        if self.ip_addy != other.ip_addy:
            return self.ip_addy

    def __str__(self):
        return f'date accessed: {self.date} | ip address: {self.ip_addy} | name of site: {self.name_of_site} | bytes accessed: {self.bytes}'



if __name__ == '__main__':
    domain_test = Domain('1/16/20 18:52','137.155.8.184','http://example.net/',2893)
    print(domain_test)
