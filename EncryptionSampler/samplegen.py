#!/usr/bin/env python

import hashlib

encryptions = ["BLAKE2b512", "BLAKE2s256", "MD4", "MD5", "MD5-SHA1", "RIPEMD160", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "blake2b", "blake2b512", "blake2s", "blake2s256",
    "md4", "md5", "md5-sha1", "ripemd160", "sha1", "sha224", "sha256", "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512", "whirlpool"]


def main():
    for algs in encryptions:
        encrypt(algs)


def encrypt(encryption):
	h = hashlib.new(encryption)
	h.update(b"Sample Text")
	h.hexdigest()

	print("Encryption: [" + encryption + "] -> " + h.hexdigest())
	
if __name__ == '__main__':
	main()
