
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	
   if (  tab.active==true && tab.url.indexOf("opensea") != -1  )//&& tab.url.indexOf("create") == -1
   {	
		chrome.tabs.sendMessage(tabId, {page_updated: true, chinfo:changeInfo.status, tb:tab.status, chUrl:changeInfo.url, tbUrl:tab.url, tabim:tab});
   }
}); 