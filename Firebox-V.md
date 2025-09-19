# Firebox-V Virtual Edtion (VMware Install)
* Download the .OVA from [Watchguard Website](https://software.watchguard.com/SoftwareDownloads?current=true&familyId=a2R2A000001YGvTUAW)
* Install the OVA in the VMware as normal
* Start up the Watchguard(WG) VM and wait until you see the login prompt in the console
* Shut down the WG VM
* In VMware, edit the settings in a fully function Debian distr machine
    * Actions -> Edit Settings -> Add New Device -> Existing Hard Disk
* Check the new disk id using ```sudo lsblk```. You should search for a disk with 8 partitions. In my case the disk is ```sdb```
```bash
### Create the certificate ###
mkdir cert
cd cert
openssl ecparam -name sect163k1 -genkey -noout -out private_key.pem
openssl ec -in private_key.pem -pubout -out public_key.pem

### Change the certificate ###
mkdir /mnt/firebox
mount /dev/sdb2 /mnt/firebox
cat public_key.pem > /mnt/firebox/etc/lickey.pem
sed -i -e "s/Product = utm/Product = base/" /mnt/firebox/info.txt
umount /dev/sdb2
rm -rf /mnt/firebox

### Change the serial number ###
mkdir /mnt/firebox
mount /dev/sdb5 /mnt/firebox
echo FVE117F24D585 > /mnt/firebox/serial
umount /dev/sdb5
rm -rf /mnt/firebox

### Generate the license ###
cd ..
git clone https://github.com/amnemonic/wg_firebox
cd wg_firebox

### Edit the 'aftermarket_lic.txt' changing the version, wg name, licenses and expiration dates ###
python3 sign_feature_key.py aftermarket_lic.txt ../cert/private_key.pem
**Signature in file aftermarket_lic.txt overwritten**

python3 verify_feature_key.py aftermarket_lic.txt ../cert/public_key.pem
**Success! This is correct feature key**

cat aftermarket_lic.txt
```
* In VMware, edit the settings in the Debian distr machine
    * Actions -> Edit Settings -> Wathguard Disk -> Remove Device
* Start up the WG VM
* Configure IP address 
* Access via GUI and add the output from the ```aftermarket_lic.txt```
    * System -> Feature Key -> Yes, I have a local copy of the feature key
    

----
[Source](https://github.com/amnemonic/wg_firebox/issues/4#issuecomment-3312606483)

