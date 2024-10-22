class Disk:
    def __init__(self, total, used):
        self.total = int(total)
        self.used = int(used)
        self.free = (int(total) - int(used))
        self.used_perc = self.used / self.total * 100
    

disk1 = Disk(10, 2)
disk2 = Disk(20, 5)
disks = [disk1, disk2]
disks.sorted = sorted(disks)
print(disk1.free)
print(disk1.used_perc)
print(disks)