## ngspice 
[Download](https://ngspice.sourceforge.io/download.htm)<br>

### Install on Ubuntu
1. Download [ngspice-45.2.tar.gz](https://sourceforge.net/projects/ngspice/files/ng-spice-rework/45.2/)
2. `tar -xzvf ngspice-45.2.tar.gz`
3. `cd ngspice-45.2`
4. `sudo ./compile_linux.sh`

### simulation
`ngspice -b bipamp.cir`<br>
`ngspice -b OpAmp.cir`<br> 
`ngspice -b rc_filter.cir`<br>

### [tutorial](https://ngspice.sourceforge.io/ngspice-tutorial.html)
![](https://ngspice.sourceforge.io/tutorial-images/fig10.png)

Spice netlist: `OpAmp.cir`<br>

```
.title Inverting OpAmp amplifier
*file OpAmp.cir
.include LF356.MOD
XU1 3 2 7 4 6 LF356/NS
R1 2 in 1k
Vin in 0 dc 0 ac 1
Vp 7 0 5
Vm 4 0 -5
Vin+ 3 0 0
R2 6 2 100k
.control
dc Vin -50m 50m 2m
set gnuplot_terminal="png"
run
gnuplot gp v(in) v(6)
.endc
.end
```
