cd C:\OpenSSL-Win32\bin
openssl pkcs12 -export -out  C:\sslforfree\certificate.pfx -inkey  C:\sslforfree\private.key -in  C:\sslforfree\certificate.crt -certfile  C:\sslforfree\ca_bundle.crt
