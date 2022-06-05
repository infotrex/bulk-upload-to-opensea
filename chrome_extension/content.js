var girdi = false;
// Başlangıç
chrome.runtime.onMessage.addListener(
  function(request, sender) {
	if(request.page_updated === true && request.tbUrl != null)
	{
		if(girdi == false)
		{  	
			girdi= true;
			let timerId = setInterval(() => testim(), 5000);
			function testim()
			 {
				const targetNode = getElementByXpath('//h1[text()="Oops, something went wrong"]');
				if(targetNode != null){
					clearInterval(timerId); clearTimeout(myTimeout); girdi= false; 
					setTimeout(() => {window.history.back();}, 2000);
				}
				const problemNode = getElementByXpath('//pre[contains(@style,"word-wrap")]');
				if(problemNode != null){
					clearInterval(timerId); clearTimeout(myTimeout); girdi= false; 
					setTimeout(() => {window.location.href=window.location.href;}, 2000);
				}
				const errorNode = getElementByXpath('//span[text()="Error adding your item: Failed to fetch"]');
				const AllmostNode = getElementByXpath('//h4[text()="Almost done"]');
				if(errorNode != null && AllmostNode == null){
					const createButtonNode = getElementByXpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button');
					clearInterval(timerId); clearTimeout(myTimeout); girdi= false; 
					setTimeout(() => {createButtonNode.click();}, 4000);
				}
				const pageIsLostNode = getElementByXpath('//h1[text()="This page is lost."]');
				if(pageIsLostNode != null){
					clearInterval(timerId); clearTimeout(myTimeout); girdi= false; 
					setTimeout(() => {window.location.href=window.location.href;}, 4000);
				}
			 }
			const myTimeout = setTimeout(() => { clearInterval(timerId); girdi= false;}, 120000);
		}
	}
  }
);
// Başlangıç 
function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
//
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


