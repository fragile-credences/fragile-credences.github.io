---
layout: post
title: "How to circumvent Sci-Hub ISP block"
image: /images/sci-hub-proxy.png
---

![](/images/sci-hub-proxy.png)

In the UK, many internet service providers block [Sci-Hub](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5832410/). Fortunately, a simple proxy is enough to circumvent this (you don't even need a VPN).

Routing requests through a suitable[^bl] proxy lets you open Sci-Hub in your regular browser as if it weren't blocked.

[^bl]: Obviously, the proxy must not itself be on a network that blocks Sci-Hub. I have not come across any proxy that blocks Sci-Hub in this way.

Routing all your traffic through a proxy may come with privacy and security concerns, and will slow your connection a bit. We want to use our proxy only for accessing Sci-Hub.

You can use extensions like [ProxySwitchy](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif) to tell your browser to automatically use certain proxies, or no proxy at all, for sets of websites that you define.

Unfortunately, this extension, and others like it, require permissions to insert arbitrary JavaScript into *any* page you visit (the web store accurately explains that the extension can "read and change all your data on the websites you visit"). That's likely due to insufficiently granular permission definitions by Chrome, and is not the fault of the presumably well-intentioned extension authors. But it freaks me out a little bit ([bad things have happened](https://robertheaton.com/2018/07/02/stylish-browser-extension-steals-your-internet-history/)).

Luckily, we can achieve the same effect by writing our own *proxy auto-configuration file*. A proxy auto-configuration or PAC file contains just a single JavaScript function like this:

```javascript
function FindProxyForURL (url, host) {
  
  // Sci-Hub requests
  if (shExpMatch(host, 'sci-hub.se')) {

                  // Your proxy address and port number
    return 'PROXY 123.456.789:9279'; 
  }

  // All other requests
  return 'DIRECT';
}
```

We can instruct the operating system to read this file[^proxyWIN]. Search for instructions on Google ([example](https://www.google.com/search?q=proxy+auto+configuration+file+mac+os)).

[^proxyWIN]: One gotcha is that Windows 10 [forces you](https://docs.microsoft.com/en-us/troubleshoot/browsers/cannot-read-pac-file) to call your PAC file from a web server; it cannot be a local file (??!). To work around this, you can upload your file as a [Gist](https://gist.github.com/) and link to the `/raw`.

The first time you use the proxy to access Sci-Hub, the browser will ask you for the username and password to your proxy server.

There are many free proxies on the Internet, but I find that using the services of an actual for-profit proxy company is well worth it, for the greater speed and reliability. Currently [webshare.io](https://www.webshare.io/proxy-server) offers 1 GB per month free, which is quite a lot of Sci-Hub PDFs. After that you can get 250 GB for $2.99 per month.[^webshare]


[^webshare]: Their home page exemplifies a dark pattern by not showing the pricing by the GB; it just says you get 'up to unlimited' bandwidth. You'll be able to see the actual pricing after you create an account.


### Step by step instructions
1. Create an account on webshare.io
2. Choose a proxy from your list, and copy its address and port number into your PAC file, following the pattern above.
3. Set your operating system to read its proxy settings from this PAC file. Instructions for this are easy to Google ([example](https://www.google.com/search?q=proxy+auto+configuration+file+mac+os)).
4. Open Sci-Hub in your browser. The first time you do this, it should ask for your proxy username and password. You can find these in your webshare.io account.
5. Don't forget to only use Sci-Hub to look at really old papers that have lapsed into the public domain :)