// Domestic DNS server
const domesticNameservers = [
  "https://223.5.5.5/dns-query",
  "https://223.6.6.6/dns-query"
];
// Foreign DNS server
const foreignNameservers = [
  "https://223.5.5.5/dns-query",
  "https://223.6.6.6/dns-query"
];
// Uncomment the following lines if you want to use foreign DNS servers and comment the above foreignNameservers.
// const foreignNameservers = [
//   "https://1.1.1.1/dns-query",
//   "https://1.0.0.1/dns-query"
// ];

// TUN configuration
const tunConfig = {
  "enable": true,
  "auto-route": true,
  "auto-redirect": true,
  "auto-detect-interface": true,
  "dns-hijack": [
    "any:53"
  ],
  "exclude-interface": [
    "Tailscale"
  ],
  "route-exclude-address": [
    "127.0.0.1/8",
    "::1/128",
    "10.0.0.0/8",
    "100.64.0.0/10",
    "169.254.0.0/16",
    "172.16.0.0/12",
    "192.168.0.0/16",
    "fc00::/7",
    "fe80::/10",
    "fd7a:115c:a1e0::/48"
  ],
  "strict-route": true
};
// DNS configuration
const dnsConfig = {
  "enable": true,
  "listen": ":1053",
  "ipv6": true,
  "ipv6-timeout": 300,
  "use-system-hosts": true,
  "respect-rules": true,
  "prefer-h3": true,
  "cache-algorithm": "arc",
  "enhanced-mode": "fake-ip",
  "fake-ip-range": "198.18.0.1/16",
  "fake-ip-filter": [
    // Custom rules
    "+.tailbecea.ts.net",
    // From @vernesong/OpenClash, @Hackl0us/SS-Rule-Snippet, and others.
    // Local and special-use domains
    "*.home.arpa",
    "*.example",
    "*.invalid",
    "*.lan",
    "*.local",
    "*.localdomain",
    "*.localhost",
    "*.test",
    // Public domains, sorted by DNS hierarchy
    "*.mcdn.bilivideo.cn",
    "+.battlenet.com.cn",
    "*.time.edu.cn",
    "time.*.edu.cn",
    "*.kuwo.cn",
    "music.migu.cn",
    "*.music.migu.cn",
    "*.ntp.org.cn",
    "+.wggames.cn",
    "+.wotgame.cn",
    "+.wowsgame.cn",
    "music.163.com",
    "*.music.163.com",
    "mesu.apple.com",
    "swcdn.apple.com",
    "swdist.apple.com",
    "swdownload.apple.com",
    "swquery.apple.com",
    "swscan.apple.com",
    "time.*.apple.com",
    "*.router.asus.com",
    "heartbeat.belkin.com",
    "*.ffxiv.com",
    "*.finalfantasyxiv.com",
    "detectportal.firefox.com",
    "alt1-mtalk.google.com",
    "alt2-mtalk.google.com",
    "alt3-mtalk.google.com",
    "alt4-mtalk.google.com",
    "alt5-mtalk.google.com",
    "alt6-mtalk.google.com",
    "alt7-mtalk.google.com",
    "alt8-mtalk.google.com",
    "lens.l.google.com",
    "mtalk.google.com",
    "mtalk-dev.google.com",
    "mtalk-staging.google.com",
    "mtalk4.google.com",
    "joox.com",
    "api.joox.com",
    "songsearch.kugou.com",
    "trackercdn.kugou.com",
    "*.linksys.com",
    "*.linksyssmartwifi.com",
    "xbox.*.microsoft.com",
    "xbox.*.*.microsoft.com",
    "msftconnecttest.com",
    "*.msftconnecttest.com",
    "msftncsi.com",
    "*.msftncsi.com",
    "resolver1.opendns.com",
    "localhost.ptlogin2.qq.com",
    "dl.stream.qqmusic.qq.com",
    "isure.stream.qqmusic.qq.com",
    "localhost.sec.qq.com",
    "aqqmusic.tc.qq.com",
    "amobile.music.tc.qq.com",
    "mobileoc.music.tc.qq.com",
    "streamoc.music.tc.qq.com",
    "y.qq.com",
    "*.y.qq.com",
    "api-jooxtt.sanook.com",
    "*.square-enix.com",
    "music.taihe.com",
    "musicapi.taihe.com",
    "time1.cloud.tencent.com",
    "xnotify.xboxlive.com",
    "*.*.xboxlive.com",
    "*.xiami.com",
    "+.market.xiaomi.com",
    "ntp.*.com",
    "ntp1.*.com",
    "ntp2.*.com",
    "ntp3.*.com",
    "ntp4.*.com",
    "ntp5.*.com",
    "ntp6.*.com",
    "ntp7.*.com",
    "time.*.com",
    "time1.*.com",
    "time2.*.com",
    "time3.*.com",
    "time4.*.com",
    "time5.*.com",
    "time6.*.com",
    "time7.*.com",
    "time.*.gov",
    "*.126.net",
    "+.nflxvideo.net",
    "+.srv.nintendo.net",
    "+.wargaming.net",
    "proxy.golang.org",
    "+.pool.ntp.org",
    // Generic wildcard domains
    "+.stun.*.*",
    "+.stun.*.*.*",
    "+.stun.*.*.*.*"
  ],
  "default-nameserver": [...domesticNameservers],
  "nameserver": [...foreignNameservers],
  "proxy-server-nameserver": [...domesticNameservers],
  "direct-nameserver": [...domesticNameservers],
  "direct-nameserver-follow-policy": false,
  "nameserver-policy": {
    "+.tailbecea.ts.net": ["100.100.100.100#Tailscale"],
    "geosite:cn,steam@cn,category-games@cn,microsoft@cn,apple@cn": domesticNameservers,
    "geosite:tld-!cn,geolocation-!cn,gfw,google-gemini,google,youtube,telegram,openai,bluesky,twitter,twitch,netflix,disney,docker": foreignNameservers
  }
};
// Sniffer configuration
const snifferConfig = {
  "enable": true,
  "force-dns-mapping": true,
  "parse-pure-ip": true,
  "sniff": {
    "HTTP": {
      "ports": [80, "8080-8880"],
      "override-destination": true
    },
    "TLS": {
      "ports": [443, 8443]
    },
    "QUIC": {
      "ports": [443, 8443]
    }
  },
  "skip-domain": [
    "Mijia Cloud",
    "dlg.io.mi.com",
    "+.push.apple.com",
    "+.apple.com",
    "alt1-mtalk.google.com",
    "alt2-mtalk.google.com",
    "alt3-mtalk.google.com",
    "alt4-mtalk.google.com",
    "alt5-mtalk.google.com",
    "alt6-mtalk.google.com",
    "alt7-mtalk.google.com",
    "alt8-mtalk.google.com",
    "mtalk-dev.google.com",
    "mtalk-staging.google.com",
    "mtalk.google.com",
    "mtalk4.google.com"
  ],
  "skip-dst-address": [
    "91.105.192.0/23",
    "91.108.4.0/22",
    "91.108.8.0/21",
    "91.108.16.0/21",
    "91.108.56.0/22",
    "95.161.64.0/20",
    "149.154.160.0/20",
    "185.76.151.0/24",
    "2001:67c:4e8::/48",
    "2001:b28:f23c::/47",
    "2001:b28:f23f::/48",
    "2a0a:f280:203::/48"
  ]
};
// Profile configuration
const profileConfig = {
  "store-selected": true,
  "store-fake-ip": true
}
// Rule Providers configuration
const ruleProviderYaml = {
  "type": "http",
  "format": "yaml",
  "interval": 86400
};
// Rule Providers configuration
const ruleProviders = {
  "adrules": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adrules_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/adrules_Domain.yaml"
  },
  "private_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/private_IP.yaml"
  },
  "private_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/private_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/private_Domain.yaml"
  },
  "blacklistrules-unlock_game": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockedgames_domainonly.yaml",
    "path": "./ruleset/paloexiz/blockedgames_domainonly.yaml"
  },
  "blacklistrules-unlock_nogame": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/unlock/clash/blockeddomains_nogame_domainonly.yaml",
    "path": "./ruleset/paloexiz/blockeddomains_nogame_domainonly.yaml"
  },
  "blacklistrules-security_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_domainonly.yaml",
    "path": "./ruleset/paloexiz/anonymityservice_domainonly.yaml"
  },
  "blacklistrules-security_process": {
    ...ruleProviderYaml,
    "behavior": "classical",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/security/clash/anonymityservice_processnameonly.yaml",
    "path": "./ruleset/paloexiz/anonymityservice_processnameonly.yaml"
  },
  "blacklistrules-boost_game": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_gameonly_domainonly.yaml",
    "path": "./ruleset/paloexiz/slowdomains_gameonly_domainonly.yaml"
  },
  "blacklistrules-boost_nogame": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/individual/boost/clash/slowdomains_nogame_domainonly.yaml",
    "path": "./ruleset/paloexiz/slowdomains_nogame_domainonly.yaml"
  },
  "steam": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Steam_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Steam_Domain.yaml"
  },
  "copilot_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/Copilot_IP.yaml"
  },
  "copilot_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Copilot_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Copilot_Domain.yaml"
  },
  "gemini": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/google-gemini_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/google-gemini_Domain.yaml"
  },
  "adobeactivation": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/adobe-activation_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/adobe-activation_Domain.yaml"
  },
  "googlefcm": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/googlefcm_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/googlefcm_Domain.yaml"
  },
  "z-library": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/z-library_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/z-library_Domain.yaml"
  },
  "bluesky": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/artifact/other/clash/bluesky/bluesky.yaml",
    "path": "./ruleset/paloexiz/bluesky.yaml"
  },
  "linuxdo": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/linuxdo_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/linuxdo_Domain.yaml"
  },
  "twitter_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/twitter_IP.yaml"
  },
  "twitter_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitter_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/twitter_Domain.yaml"
  },
  "github": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/github_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/github_Domain.yaml"
  },
  "gitlab": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gitlab_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/gitlab_Domain.yaml"
  },
  "onedrive": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/onedrive_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/onedrive_Domain.yaml"
  },
  "microsoft": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Microsoft_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Microsoft_Domain.yaml"
  },
  "openai": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/openai_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/openai_Domain.yaml"
  },
  "anthropic": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/anthropic_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/anthropic_Domain.yaml"
  },
  "discord": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/discord_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/discord_Domain.yaml"
  },
  "aliyun": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/aliyun_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/aliyun_Domain.yaml"
  },
  "cloudflare": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cloudflare_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/cloudflare_Domain.yaml"
  },
  "docker": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/docker_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/docker_Domain.yaml"
  },
  "homebrew": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/homebrew_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/homebrew_Domain.yaml"
  },
  "python": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/python_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/python_Domain.yaml"
  },
  "icloud": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/icloud_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/icloud_Domain.yaml"
  },
  "apple": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/apple_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/apple_Domain.yaml"
  },
  "youtube": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/youtube_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/youtube_Domain.yaml"
  },
  "google_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/Google_IP.yaml"
  },
  "google_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Google_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Google_Domain.yaml"
  },
  "twitch": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/twitch_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/twitch_Domain.yaml"
  },
  "niconico": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/niconico_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/niconico_Domain.yaml"
  },
  "pixiv": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Pixiv_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Pixiv_Domain.yaml"
  },
  "netflix_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/netflix_IP.yaml"
  },
  "netflix_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/netflix_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/netflix_Domain.yaml"
  },
  "disney": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/disney_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/disney_Domain.yaml"
  },
  "bilibili": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/bilibili_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/bilibili_Domain.yaml"
  },
  "spotify": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/spotify_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/spotify_Domain.yaml"
  },
  "dmm": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/dmm_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/dmm_Domain.yaml"
  },
  "telegram_ip": {
    ...ruleProviderYaml,
    "behavior": "ipcidr",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_IP.yaml",
    "path": "./ruleset/paloexiz/third_party/Telegram_IP.yaml"
  },
  "telegram_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/Telegram_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/Telegram_Domain.yaml"
  },
  "gfw": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/gfw_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/gfw_Domain.yaml"
  },
  "applications": {
    ...ruleProviderYaml,
    "behavior": "classical",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/applications.yaml",
    "path": "./ruleset/paloexiz/third_party/applications.yaml"
  },
  "cn_domain": {
    ...ruleProviderYaml,
    "behavior": "domain",
    "url": "https://fastly.jsdelivr.net/gh/Paloexiz/blacklist-rules@main/third_party/clash/cn_Domain.yaml",
    "path": "./ruleset/paloexiz/third_party/cn_Domain.yaml"
  }
};
// Rules
const rules = [
  "RULE-SET, adrules, AdBlock",
  "RULE-SET, private_ip, DIRECT, no-resolve",
  "RULE-SET, private_domain, DIRECT",
  "RULE-SET, blacklistrules-unlock_game, Game Unlocking",
  "RULE-SET, blacklistrules-unlock_nogame, Proxy",
  "RULE-SET, blacklistrules-security_domain, Safe Browse",
  "RULE-SET, blacklistrules-security_process, Safe Browse",
  "RULE-SET, blacklistrules-boost_game, Game Boosting",
  "RULE-SET, blacklistrules-boost_nogame, Proxy",
  "RULE-SET, steam, Steam",
  "RULE-SET, adobeactivation, Adobe Activation Service",
  "RULE-SET, googlefcm, Google FCM",
  "RULE-SET, z-library, Z-Library",
  "RULE-SET, bluesky, Bluesky",
  "RULE-SET, linuxdo, LINUX DO",
  "RULE-SET, twitter_ip, Twitter",
  "RULE-SET, twitter_domain, Twitter",
  "RULE-SET, anthropic, Claude",
  "RULE-SET, openai, ChatGPT",
  "RULE-SET, copilot_ip, Copilot",
  "RULE-SET, copilot_domain, Copilot",
  "RULE-SET, gemini, Gemini",
  "RULE-SET, github, GitHub",
  "RULE-SET, gitlab, GitLab",
  "RULE-SET, onedrive, OneDrive",
  "RULE-SET, microsoft, Microsoft",
  "RULE-SET, discord, Discord",
  "RULE-SET, aliyun, Aliyun",
  "RULE-SET, cloudflare, Cloudflare",
  "RULE-SET, docker, Docker",
  "RULE-SET, homebrew, Homebrew",
  "RULE-SET, python, Python",
  "RULE-SET, icloud, iCloud",
  "RULE-SET, apple, Apple",
  "RULE-SET, youtube, Youtube",
  "RULE-SET, google_ip, Google",
  "RULE-SET, google_domain, Google",
  "RULE-SET, twitch, Twitch",
  "RULE-SET, niconico, Niconico",
  "RULE-SET, pixiv, Pixiv",
  "RULE-SET, netflix_ip, Netflix",
  "RULE-SET, netflix_domain, Netflix",
  "RULE-SET, disney, Disney",
  "RULE-SET, bilibili, Bilibili",
  "RULE-SET, spotify, Spotify",
  "RULE-SET, dmm, DMM",
  "RULE-SET, telegram_ip, Telegram",
  "RULE-SET, telegram_domain, Telegram",
  "RULE-SET, gfw, Proxy",
  "RULE-SET, applications, Domestic",
  "RULE-SET, cn_domain, Domestic",
  "GEOIP, CN, Domestic, no-resolve",
  "MATCH, Others"
];
// Common options for group
const groupBaseOption = {
  "interval": 720,
  "timeout": 3000
};

// Program Entry
function main(config) {
  const proxyCount = config?.proxies?.length ?? 0;
  const proxyProviderCount =
    typeof config?.["proxy-providers"] === "object" ? Object.keys(config["proxy-providers"]).length : 0;
  if (proxyCount === 0 && proxyProviderCount === 0) {
    throw new Error("Cannot Find any proxy providers in configuration.");
  }
  let defaultProxyGroups = ["Proxy", "All Nodes", "Minimum delay", "Fallback", "Load Balancing (Hashing)", "Load Balancing (Round Robin)", "DIRECT"];
  let defaultDirectGroups = ["DIRECT", "Proxy", "All Nodes", "Minimum delay", "Fallback", "Load Balancing (Hashing)", "Load Balancing (Round Robin)"];

  // Replace proxy groups in original configuration
  config["proxy-groups"] = [
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Proxy",
      "type": "select",
      "proxies": ["All Nodes", "Minimum delay", "HK Nodes", "TW Nodes", "JP Nodes", "US Nodes", "SG Nodes", "UK Nodes", "Fallback", "Load Balancing (Hashing)", "Load Balancing (Round Robin)"]
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "All Nodes",
      "type": "select",
      "include-all": true
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "HK Nodes",
      "filter": "(?i)港|hk|hongkong|hong kong",
      "type": "select",
      "include-all": true
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "TW Nodes",
      "type": "select",
      "include-all": true,
      "filter": "(?i)台|tw|twn|taiwan"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "JP Nodes",
      "type": "select",
      "include-all": true,
      "filter": "(?i)日本|jp|japan"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "US Nodes",
      "type": "select",
      "include-all": true,
      "filter": "(?i)美国|us|unitedstates|united states"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "SG Nodes",
      "type": "select",
      "include-all": true,
      "filter": "(?i)新加坡|sg|Singapore"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "UK Nodes",
      "type": "select",
      "include-all": true,
      "filter": "(?i)英国|uk|gbr"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Minimum delay",
      "type": "url-test",
      "tolerance": 100,
      "include-all": true,
      "exclude-filter": "剩余流量|remaining-traffic|套餐到期|plan-expired|提前用完买重置包|距离下次重置剩余|remaining-reset"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Fallback",
      "type": "fallback",
      "include-all": true,
      "exclude-filter": "剩余流量|remaining-traffic|套餐到期|plan-expired|提前用完买重置包|距离下次重置剩余|remaining-reset"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Load Balancing (Hashing)",
      "type": "load-balance",
      "strategy": "consistent-hashing",
      "include-all": true,
      "exclude-filter": "剩余流量|remaining-traffic|套餐到期|plan-expired|提前用完买重置包|距离下次重置剩余|remaining-reset"
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Load Balancing (Round Robin)",
      "type": "load-balance",
      "strategy": "round-robin",
      "include-all": true,
      "exclude-filter": "剩余流量|remaining-traffic|套餐到期|plan-expired|提前用完买重置包|距离下次重置剩余|remaining-reset"
    },
    {
      ...groupBaseOption,
      "url": "https://discord.com",
      "name": "Discord",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://telegram.org",
      "name": "Telegram",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://chatgpt.com",
      "expected-status": "200",
      "name": "ChatGPT",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://claude.ai",
      "expected-status": "200",
      "name": "Claude",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://copilot.microsoft.com",
      "expected-status": "200",
      "name": "Copilot",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://gemini.google.com",
      "expected-status": "200",
      "name": "Gemini",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://bilibili.com",
      "name": "Bilibili",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://disney.com",
      "expected-status": "200",
      "name": "Disney",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://dmm.com",
      "expected-status": "200",
      "name": "DMM",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://netflix.com",
      "expected-status": "200",
      "name": "Netflix",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://niconico.com",
      "expected-status": "200",
      "name": "Niconico",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://pixiv.net",
      "expected-status": "200",
      "name": "Pixiv",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://spotify.com",
      "expected-status": "200",
      "name": "Spotify",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://twitch.tv",
      "name": "Twitch",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://youtube.com",
      "name": "Youtube",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://z-library.sk",
      "name": "Z-Library",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://bsky.app",
      "name": "Bluesky",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://linux.do",
      "name": "LINUX DO",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://x.com",
      "name": "Twitter",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://icloud.com",
      "name": "iCloud",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://onedrive.com",
      "name": "OneDrive",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://aliyun.com",
      "name": "Aliyun",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://cloudflare.com",
      "name": "Cloudflare",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://docker.com",
      "name": "Docker",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://brew.sh",
      "name": "Homebrew",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://www.python.org",
      "name": "Python",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://github.com",
      "name": "GitHub",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://gitlab.com",
      "name": "GitLab",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://apple.com",
      "name": "Apple",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://google.com",
      "name": "Google",
      "type": "select",
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://microsoft.com",
      "name": "Microsoft",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://store.steampowered.com",
      "name": "Steam",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://dns.aliyun.com",
      "name": "Adobe Activation Service",
      "type": "select",
      "proxies": ["REJECT", "DIRECT", "Proxy"]
    },
    {
      ...groupBaseOption,
      "url": "https://dns.aliyun.com",
      "name": "AdBlock",
      "type": "select",
      "proxies": ["REJECT", "DIRECT", "Proxy"]
    },
    {
      ...groupBaseOption,
      "url": "https://dns.alidns.com",
      "name": "Domestic",
      "type": "select",
      "proxies": ["DIRECT", "Proxy", "Minimum delay", "Fallback", "Load Balancing (Hashing)", "Load Balancing (Round Robin)"]
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Game Boosting",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Game Unlocking",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://mtalk.google.com",
      "name": "Google FCM",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Others",
      "type": "select",
      "proxies": [...defaultDirectGroups]
    },
    {
      ...groupBaseOption,
      "url": "https://www.gstatic.com/generate_204",
      "name": "Safe Browse",
      "type": "select",
      "include-all": true,
      "proxies": [...defaultProxyGroups]
    }
  ];

  // Replace Original Rules
  config["tun"] = tunConfig;
  config["dns"] = dnsConfig;
  config["sniffer"] = snifferConfig;
  config["profile"] = profileConfig;
  config["rules"] = rules;
  config["rule-providers"] = ruleProviders;

  return config;
}
