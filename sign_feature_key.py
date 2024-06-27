import os
import sys

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


def inst_symbol(my_str, group=10, char=' '):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))


if len(sys.argv)!=3: print(f'Error!\nUsage: {os.path.basename(sys.argv[0])} <feature_key_file> <private_key.pem>', file=sys.stderr) ; exit(1)


feature_key = open(sys.argv[1],'r').read()                                        # <feature_key_file>
private_key = load_pem_private_key(open(sys.argv[2],'rb').read(), password=None)  # <private_key.pem>



signature_start = feature_key.find("Signature:")
if signature_start == -1:
    raise ValueError("Signature field not found in the license data.")


data_before_signature = feature_key[:signature_start]
data_after_signature  = feature_key[signature_start + len("Signature:"):]



#remove all white characters from license
license_normalized = b''.join([char.encode() for char in data_before_signature if char not in ['\t', '\n', '\x0b','\x0c', '\r', ' ']])

#parse signature hex value
#signature = bytes.fromhex(data_after_signature.strip().replace('-',''))
signature = private_key.sign(license_normalized, ec.ECDSA(hashes.SHA1()))
new_signature = 'Signature: '+inst_symbol(signature.hex(),16,'-')
print(new_signature)


open(sys.argv[1],'w', newline='\n').write(data_before_signature+new_signature)
print('Signature in file {} overwritten'.format(sys.argv[1]))
