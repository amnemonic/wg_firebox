# WatchGuard Fireware/Firebox Feature Keys – Reference


This document lists common **WatchGuard Fireware / Firebox feature keys** and what they enable.
Use it to quickly understand license capabilities when reading feature keys from your devices.

- **Links:** Where possible, each item includes an official documentation link

## Security & Threat Protection

- **WEBBLOCKER** — URL/content filtering service that categorizes and blocks sites. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/webblocker/webblocker_about_c.html)
- **SPAMBLOCKER** — Anti-spam service for SMTP/POP3 proxies to block unsolicited email. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/spamblocker/spam_about_c.html)
- **AV** — Gateway AntiVirus scans traffic at the network edge for malware. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/gateway_av/gateway_av_intrusion_prev_c.html)
- **INTELLIGENT_AV** — Machine-learning antivirus engine (Cylance-based) for zero-day malware. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/intelligentav/intelligentav_about_c.html)
- **IPS** — Intrusion Prevention Service to detect and block network threats. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/ips/ips_about_c.html)
- **RED** — Reputation Enabled Defense to block connections to known bad sites. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/reputation_enabled_defense/red_about_c.html)
- **APT** — APT Blocker: sandboxing service for advanced malware/ransomware. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/apt/apt_about_c.html)
- **APP_CONTROL** — Application Control: identify and control app usage in policies. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/app_control/app_control_about_c.html)
- **DNSWATCH** — DNS filtering & anti-phishing service that monitors DNS requests. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/dnswatch/dnswatch_intro_c.html)
- **MOBILE_SECURITY_USER** — Licensed number of Mobile Security users. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/other/chapters/mobile-security.html)

## VPN & Remote Access

- **IPSEC_VPN** — IPSec VPN (BOVPN, Mobile VPN with IPSec). [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/bovpn/manual/bovpn_manual_about_c.html)
- **SSLVPN_USER** — Licensed capacity for Mobile VPN with SSL users. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/mvpn/ssl/mvpn_ssl_about_c.html)
- **L2TP_USER** — Licensed capacity for Mobile VPN with L2TP users. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/mvpn/l2tp/l2tp_vpn_about_c.html)
- **ACCESS_PORTAL** — Clientless VPN portal for web apps, RDP and SSH access via browser. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/access%20portal/access_portal_about.html)
- **IPSEC_CRYPTO_GOST** — Enables GOST cryptographic transforms for IPsec/IKEv2 where required. [Docs](https://www.rfc-editor.org/rfc/rfc9385.pdf)
- **VPN_CERT** — Third‑party VPN certificate support entitlement.

## Networking & Routing

- **VLAN** — Virtual LAN interfaces and tagging support on the Firebox. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/networksetup/vlans_about_c.html)
- **QOS** — Quality of Service bandwidth and priority controls. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/qos_trafficmanagement/traffic_mgmt_qos_about_c.html)
- **POLICY_ROUTING** — Policy-based routing to direct traffic based on policy criteria. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/policies/policy_mgr_about_wsm.html)
- **BGP** — Dynamic routing using BGP (FRR) on Fireware. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/dynamicrouting/bgp_about_c.html)
- **OSPF** — Dynamic routing with OSPF. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/dynamicrouting/ospf_about_c.html)
- **SERVER_LOAD_BALANCING** — Distribute traffic among multiple internal servers. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/nat/server_load_balancing_config_c.html)
- **WAN_FAILOVER** — Multi-WAN failover for resilience when a WAN link goes down. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/multiwan/failover_configure_c.html)
- **LINK_AGGREGATION** — LAG (802.1AX/LACP) to bond interfaces for bandwidth & redundancy. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Devices/managed/network_config_link_aggregation_about.html)
- **FIRECLUSTER** — High availability (active/active or active/passive clustering). [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/ha/cluster_about_wsm.html)
- **MULTI_WAN** — Multi‑WAN feature entitlement. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/multiwan/multiwan_about_c.html)
- **LOAD_BALANCE** — Multi‑WAN load balancing entitlement.
- **VIP_LOAD_BALANCING** — Virtual IP load balancing entitlement.

## Visibility & Cloud

- **NETWORK_DISCOVERY** — Discovers devices on internal networks and maps them in the UI. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/network_discovery/network_discovery_web.html)
- **DASHBOARD** — Enables dashboard/visibility components (Dimension/Cloud). [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/dimension/about-dimension_d.html)
- **CLOUD_VISIBILITY** — WatchGuard Cloud visibility & reporting data retention for Firebox. [Docs](https://www.watchguard.com/help/docs/help-center/en-us/Content/en-US/WG-Cloud/Devices/device_licenses_about.html)
- **CLOUD_CONNECT** — Allows Standard Support devices to connect to WatchGuard Cloud for cloud-management (no reporting). [Docs](https://techsearch.watchguard.com/KB?SFDCID=kA16S000000WOhdSAG&lang=en_US&type=Article)
- **CLOUD_SUPPORT** — Indicates WatchGuard Support entitlement / LiveSecurity on the device. [Docs](https://www.watchguard.com/help/docs/help-center/en-us/Content/en-US/Fireware/support/lss_about_c.html)
- **DAAS_BASIC** — Dimension-as-a-Service (legacy) – basic tier for hosted Dimension/management. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/dimension/about-dimension_d.html)
- **DAAS_TOTAL** — Dimension-as-a-Service (legacy) – full/total tier for hosted Dimension/management. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/dimension/about-dimension_d.html)
- **DIMENSION_COMMAND** — WatchGuard Dimension Command (legacy centralized management).

## Licensing & Capacity

- **FW_PRO** — Fireware Pro license enabling advanced features (e.g., dynamic routing, PBR, server load balancing). [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/overview/fireware/fireware_pro_c.html)
- **XTM_PRO** — Legacy XTM Pro (older platforms) enabling advanced networking. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/overview/fireware/fireware_pro_c.html)
- **FW_STD** — Fireware Standard edition.
- **FW_USERS** — Licensed user count (model-dependent limit for authenticated users).
- **MAX_CORES** — Indicates maximum CPU cores supported/usable by the license on platform.
- **EDGE_PRO** — Alias seen in feature keys for Pro-level capabilities on some models.
- **DTEWS** — Uncommon/legacy feature flag seen in keys, no public doc reference.
- **WATCHMODE** — Audit-only mode for NFR devices to mirror/inspect traffic (demo). [Docs](https://www.watchguard.com/help/docs/fireware/12/en-US/WatchMode_Config-Guide_PDF_%28en-US%29.pdf)
- **LIVESECURITY** — LiveSecurity/Support service entitlement.
- **MODEL** — Model upgrade/entitlement field in feature key.
- **FW_RULE** — Licensed maximum number of firewall policies.
- **FW_SPEED** — Licensed maximum throughput for firewall policies (model/edition dependent).
- **VPN_SPEED** — Licensed maximum throughput for VPN policies (model/edition dependent).
- **SESSION** — Licensed maximum concurrent sessions.
- **AUTHENTICATED_USER** — Licensed maximum authenticated users.
- **AUTH_DOMAIN** — Licensed maximum authentication domains.
- **AV_SPEED** — Licensed maximum throughput for Gateway AntiVirus.
- **INTERFACE** — Licensed maximum number of network interfaces.
- **FIREWARE** — Fireware OS entitlement field.
- **FIREWARE_XTM** — Legacy Fireware XTM entitlement.
- **3DES** — 3DES encryption entitlement/legacy flag.
- **PROXY_SPEED** — Licensed maximum throughput for proxy policies.
- **XTMWARE** — Legacy XTMWARE platform flag.
- **IPSEC_CRYPTO** — IPsec cryptographic algorithm entitlement (non‑GOST).

## End of Life
- **DLP** (end-of-life as of 26 February 2025) — Data Loss Prevention: detect and block sensitive data exfiltration. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/dlp/dlp_about_c.html)
- **TDR** (end-of-life as of 30 September 2025) — Threat Detection and Response: cloud-based threat correlation & host sensors. [Docs](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/other/chapters/mobile-security.html)

## Other Keys

- **ACCESS_PORTAL_TRIAL**
- **APP_CONTROL_TRIAL**
- **APT_TRIAL**
- **AV_TRIAL**
- **AV_UPDATE**
- **BOVPN_TUNNEL**
- **DAAS_BASIC_TRIAL**
- **DAAS_TOTAL_TRIAL**
- **DIMENSION_COMMAND_TRIAL**
- **DLP_TRIAL**
- **DNSWATCH_TRIAL**
- **DTEWS_TRIAL**
- **FW**
- **HA**
- **INTELLIGENT_AV_TRIAL**
- **IPSEC_USER**
- **IPS_TRIAL**
- **IPS_UPDATE**
- **MOBILE_SECURITY** — Enforce device compliance for iOS/Android before allowing traffic.
- **MOBILE_SECURITY_USER_TRIAL**
- **MUVPN_USER**
- **NETWORK_DISCOVERY_TRIAL**
- **RED_TRIAL**
- **SPAMBLOCKER_TRIAL**
- **TDR_TRIAL**
- **WEBBLOCKER_TRIAL**
