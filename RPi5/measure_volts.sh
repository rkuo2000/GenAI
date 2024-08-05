for id in core sdram_c sdram_i sdram_p ; do \
    echo -e "$id:\t$(vcgencmd measure_volts $id)" ; \
done
