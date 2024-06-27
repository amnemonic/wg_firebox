import os
import sys

from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


if len(sys.argv)!=3: print(f'Error!\nUsage: {os.path.basename(sys.argv[0])} <feature_key_file> <lickey.pem>', file=sys.stderr) ; exit(1)


feature_key = open(sys.argv[1],'r').read()                          # <feature_key_file>
public_key  = load_pem_public_key(open(sys.argv[2],'rb').read())    # <lickey.pem>



signature_start = feature_key.find("Signature:")
if signature_start == -1:
    raise ValueError("Signature field not found in the license data.")


data_before_signature = feature_key[:signature_start]
data_after_signature  = feature_key[signature_start + len("Signature:"):]



#remove all white characters from license
license_normalized = b''.join([char.encode() for char in data_before_signature if char not in ['\t', '\n', '\x0b','\x0c', '\r', ' ']])

#parse signature hex value
signature = bytes.fromhex(data_after_signature.strip().replace('-',''))


#verify signature
try:
    public_key.verify(signature, license_normalized, ec.ECDSA(hashes.SHA1()))
    print('Success! This is correct feature key')
except Exception as e:
    if type(e) == InvalidSignature:
        print('Invalid Signature. Verification of Feature Key Failed')
    else:
        raise
