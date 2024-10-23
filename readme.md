### About this project
**This utility is intended solely for hobbyists and enthusiasts for learning and personal enjoyment. It is designed to be used on devices that have reached the end of their lifecycle or support cycle. Please use this tool responsibly and in good faith. Any commercial use, misuse, or use on production on active and supported devices is strictly discouraged.**

By using this tool, I hope to encourage the reuse of old, discarded hardware, thereby contributing to the reduction of e-waste. The authors takes no responsibility for any consequences arising from improper use of this utility. Thank you for respecting these guidelines.


### WatchGuard Firebox M270
M270 reached End of Sales (EOS) Date on July 1 of 2023 and quite often you can find them really cheap on some marketplaces. These are still decent machines and can be used in homelab by enthusiast and as learning aid. Inside the case you will find [Lanner](https://en.wikipedia.org/wiki/Lanner_Electronics) motherboard NCB-WG2511A with [Intel Atom C3558](https://www.intel.com/content/www/us/en/products/sku/97937/intel-atom-processor-c3558-8m-cache-up-to-2-20-ghz/specifications.html) processor and 4GB of DDR4/2133 RAM stick.

### License aka Feature Key
If the previous owner did factory reset of the device then to restore full firewall functionality you will need license for some fancier things like VPN, Network discovery etc. If you was lucky enough to get hands on not resetted box then pull out mSata drive from the appliance and backup the license file from directory `/licenses/` on the last (biggest) partition on drive. 

Feature key is assigned to machine by its serial number and then signed. When you enter license then its signature is checked against public key stored in `/etc/lickey.pem` on third partition:

```
-----BEGIN PUBLIC KEY-----
MEAwEAYHKoZIzj0CAQYFK4EEAAEDLAAEA8Bzr9a6TxFepuDXXSZW+tiRIWjhACAv
T7+0dndwVGH2mFqj0YdPkYpN
-----END PUBLIC KEY-----
```

### Generating your own License
To workaround issue with license we can follow one of (at least) two ways: 
1) factorize private key 
2) replace public key by our own

for obvious reasons I choose second way.

#### New keypair
Generate new keypair using openssl:
```
openssl ecparam -name sect163k1 -genkey -noout -out private_key.pem
```

Extract the public key from the private key:
```
openssl ec -in private_key.pem -pubout -out public_key.pem
```


#### Replace `lickey.pem` on Firebox filesystem
Get mSata drive out of Firebox and connect to linux machine. Assuming that disk was recognized as `sda` you can execute following commands:
```
mkdir /mnt/firebox
mount /dev/sda3 /mnt/firebox
cat public_key.pem > /mnt/firebox/etc/lickey.pem
umount /dev/sda3
```

`public_key.pem` is public key generated in previous paragraph


#### Sign License
Edit [`aftermarket_lic.txt`](https://github.com/amnemonic/wg_firebox/blob/main/aftermarket_lic.txt) file, eg. set your serial number and machine name and license items and dates then run python script:
```
sign_feature_key.py aftermarket_lic.txt private_key.pem
```
Signature will be updated in place. 


You can verify signature using second script:
```
verify_feature_key.py aftermarket_lic.txt public_key.pem
Success! This is correct feature key
```

Upload license using "Update Feature Key" option in your appliance.




### Epilogue
 - this method was tested only on my `M270` but it can be safely assumed that it should work also for `M370` `M470` `M570` and `M670`.
 - you can generate license with valid `LiveSecurity Service` and therefore upgrade Fireware OS to newer version however you have to repeat procedure of replacing `lickey.pem` because our modded key will be replaced to stock one by updater. 
 - Unfortunately starting from version **12.5.9 Update 2 and higher** of Fireware OS, WatchGuard introduced [integrity check](http://www.watchguard.com/help/docs/help-center/en-US/content/en-us/Fireware/system_status/stats_diagnostics_integrity_checks.html) of file system and when you replace `lickey.pem` then kernel will throw following error:
```
Signature did not verify
Error: integrity check failed
initrd: Failed.  Shutting down.
```

 - Latest version which can be patched this way is [12.5.4](http://ftp.watchguard.jp/Partner/Software/XTM-Firebox/Firebox-M270-M370-470-570-670/12.5.4/)

### To do (PRs are welcome)
- [ ] Try to disable integrity check. It would decrease security but for homelab that should be reasonably safe solution
- [ ] Make a list of possible entries in license file and name of each possibly with link to official description of service
- [x] Be more precise about which version introduced file system integrity check

 
### Bonus!
Hard coded bios password for `M270` with bios version V2.02 (04022018) is: `WatchGuard!`. If you were able to confirm that this password works for other WatchGuard's product let me know by opening new issue or just ping me on my twitter or whatever.

