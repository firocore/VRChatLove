from PySide6.QtCore import QObject, Signal
from collections import defaultdict

class OSCParameterStore(QObject):
    updated = Signal()

    def __init__(self):
        super().__init__()
        self.parameters = {}
        self.groups = defaultdict(set)

    def update(self, address: str, value):
        self.parameters[address] = value
        group = address.split('/')[2] if len(address.split('/')) > 2 else "other"
        self.groups[group].add(address)
        self.updated.emit()

    def get_grouped(self):
        return {group: {addr: self.parameters[addr] for addr in addrs}
                for group, addrs in self.groups.items()}
    
    def clear_all(self):
        self.parameters = {}
        self.groups = defaultdict(set)
