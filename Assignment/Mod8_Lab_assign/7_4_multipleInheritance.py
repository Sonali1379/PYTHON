class Printer:
    def print_doc(self, text):
        return f"Printing: {text}"


class Scanner:
    def scan_doc(self):
        return "Scanning document..."


class AllInOne(Printer, Scanner):
    def copy(self, text):
        scanned = self.scan_doc()
        printed = self.print_doc(text)
        return f"{scanned} Then {printed}"


if __name__ == "__main__":
    device = AllInOne()
    print(device.print_doc("Hello"))
    print(device.scan_doc())
    print(device.copy("Lab report"))
