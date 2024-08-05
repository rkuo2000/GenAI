for codec in H264 MPG2 WVC1 MPG4 MJPG WMV9 ; do \
    echo -e "$codec:\t$(vcgencmd codec_enabled $codec)" ; \
done
