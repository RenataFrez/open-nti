all:
   timeout 60 python $(shell pwd)/jti_input_socket.py
   for i in `ls file_*`; do protoc --decode_raw < $i ;done

clean:
   rm -rf $(shell pwd)/file_*
