import m5
import argparse
from m5.objects import * 

# System
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Address ranges
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# More system config stuff
system.cpu = TimingSimpleCPU()

system.membus = SystemXBar()
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

system.cpu.createInterruptController()
if m5.defines.buildEnv['TARGET_ISA'] == "x86": 
    system.cpu.interrupts[0].pio = system.membus.master
    system.cpu.interrupts[0].int_master = system.membus.slave
    system.cpu.interrupts[0].int_slave = system.membus.master

# Memory Config
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# not sure what this does
system.system_port = system.membus.slave

# ISA config
isa = str(m5.defines.buildEnv['TARGET_ISA']).lower()

# Get user x86 binary
parser = argparse.ArgumentParser()
parser.add_argument("--binary", required=True)
args = parser.parse_args()

system.workload = SEWorkload.init_compatible(args.binary)

# Start and simulate process
process = Process()
process.cmd = args.binary
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)
m5.instantiate()

print ("Beginning Simulation!")
exit_event = m5.simulate()
print ("Exiting at tick {} because {}".format(m5.curTick(), exit_event.getCause()))
