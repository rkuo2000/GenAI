## ngspice 

### Install on Ubuntu
[Download](https://ngspice.sourceforge.io/download.htm)
[ngspice-45.2](https://sourceforge.net/projects/ngspice/files/ng-spice-rework/45.2/)
1. Download ngspice-45.2.tar.gz
2. `tar -xzvf ngspice-45.2.tar.gz`
3. `cd ngspice-45.2`
4. `sudo ./compile_linux.sh`

### simulation
`ngspice -b bipamp.cir`<br>
`ngspice -b OpAmp.cir`<br> 
`ngspice -b rc_filter.cir`<br>

### example circuits
Spice netlist: `bipamp.cir`<br>

```
bipolar amplifier
* file bipamp.cir
.model BC546B npn ( IS=7.59E-15 VAF=73.4 BF=480 IKF=0.0962 NE=1.2665
+ ISE=3.278E-15 IKR=0.03 ISC=2.00E-13 NC=1.2 NR=1 BR=5 RC=0.25 CJC=6.33E-12
+ FC=0.5 MJC=0.33 VJC=0.65 CJE=1.25E-11 MJE=0.55 VJE=0.65 TF=4.26E-10
+ ITF=0.6 VTF=3 XTF=20 RB=100 IRB=0.0001 RBM=10 RE=0.5 TR=1.50E-07)
R3 vcc intc 10k
R1 vcc intb 68k
R2 intb 0 10k
Cout out intc 10u
Cin intb in 10u
VCC vcc 0 5
Vin in 0 dc 0 ac 1 sin(0 1m 500)
RLoad out 0 100k
Q1 intc intb 0 BC546B
.tran 10u 10m
.ac dec 10 10 1Meg
.control 
set gnuplot_terminal="png"
run 
gnuplot gp v(out) v(in)
.endc
.end
```
