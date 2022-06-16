<img src="src/images/fortune-cat-neko.png" width="350">

# bulk-upload-to-opensea
A cross platform python IDE implementing selenium 4<BR>
If you want to support this project or me, please check out my NFTs <BR>
https://opensea.io/collection/fortune-cat-neko and wish give it a little love or grab it.<BR>
Thank you.

  Tutorial video v1.0<BR>
  https://www.youtube.com/watch?v=yEowEDfTSpA<BR>
  ~ or ~<BR>
  Easy step by step<BR>
  https://www.youtube.com/watch?v=j0WguSodGf8<BR>
  Bulk upload to opensea - Buster: Captcha Solver<BR>
  https://www.youtube.com/watch?v=6IoyczfQxtg<BR>
  

# Pay Service
  Why need to pay? I realise some user are over requested additional feature or addon over the limitation.
  if you are really need additional function for this bulk upload please contact my twitter @klvntss and the charge will by project basis. https://www.fiverr.com/kelvintss

# Disclaimer
  This free version script are not collect or capture any information while it running.
  Make sure you are understand the all coding and process before running, please read line by line the original code before start running.
  We will not be liable for any losses and/or damages for using of our script. Use at your own risk.
  
# Changelog
  <ul>
    <li><b>Version 2.0.1 (upload_2captcha V2.py)</b><BR>
       Deleted some controls that were no longer needed for the polygon.<BR>
       Added Latest stable release: ChromeDriver
      </li>
    <li><b>Version 2.0.0 (upload_2captcha V2.py)</b><BR>
       2Captcha and Buster Solver combined in one file<BR>
       Added repetitive error checks for many possible errors that may occur on the site<BR>
       Added "chrome_extension" Please open chrome_extension folder and read the instructions<BR>
       Collection Scraper added as prototype.
      </li>
      <li><b>Version 1.9.0 (upload_2captcha.py)</b><BR>
       2Captcha Solver<BR>
       https://chrome.google.com/webstore/detail/2captcha-solver/ifibfemgeogfhoebkmokieepdoobkbpo?hl=en<BR>
        get your API-key from <a href="https://2captcha.com?from=13605454" target="_blank">2captcha.com</a><BR>
        Enabled & Solve automatically reCaptcha V2 at option page.
      </li>
      <li><b>Version 1.8.9 (upload_captcha.py)</b><BR>
       Fixed duration range selection
      </li>
    <li><b>Version 1.8.8 (upload_captcha.py)</b><BR>
        Add chrome extesion: Buster: Captcha Solver for Humans<BR>
        https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en<BR>
extension settings: Select any "speech service" and put in API key
      </li>
     <li><b>Version 1.8.1 (upload18.py)</b>
      <ul>
        <li>support "attributes" and "properties" metadata format</li>
      </ul></li>
    <li><b>Version 1.8 (upload18.py)</b>
      <ul>
        <li>Duration support added. Maximum duration is 6 months. <BR>
        *Please install "pip install python-dateutil"<BR>
          PC date format MUST set to mm/dd/yyyy
         </li>
      </ul></li>
    <li><b>Version 1.0 (upload.py)</b>
      <ul><li>Standard version</li></ul>
    </li>
  </ul>

# Instructions
<ul>
  <li>Download and extract this project in your local device (keep all files and folders that come with the repo in this folder)</li>
  <li>Download and update Python. My python version is 3.8.10 * https://www.youtube.com/watch?v=9o4gDQvVkLU</li>
   <li>Put all the NFTs images into folder “src/images” (etc 1.png), and NFTs properties metadata .json file put into folder src/json. (etc 1.json)</li>
   <li>Open this project folder with any code editor and click "open powershell " or "Terminal"</li>
   <li>Pip install requirements.txt by running the following command (pip install -r requirements.txt) <BR>
       Please install PIP for Python if “pip is not recognized as an internal or external command</li>
   <li>Run the script, type "python upload.py"</li>
   <li>Once running the script, will pop-up the application </li>
   <li>Fill in the variable for your project upload properties, </li>
     <ul>
       <li>Opensea collection link: https://www.opensea.io/collection/yourcollectionsname/<B>assets/create</b></li>
        <li>Start number 1</li>
        <li>End number 9999 or any number</li>
        <li>Default price: 0.005</li>
        <li>Title with end “#” symbol</li>
        <li>Description</li>
        <li>NFT image format "png"</li>
        <li>External link start with http….</li>
     </ul>
   <li>Click and Select the “src” folder.</li>
   <li>Click and “save this form”</li>
     <li>Click “open chrome browser” will popup a new chrome browser, login / sign-in your metamask account. Download metamask extension if don’t have</li>
     <li>Download I'm not robot captcha clicker extension link: https://chrome.google.com/webstore/detail/im-not-robot-captcha-clic/ceipnlhmjohemhfpbjdgeigkababhmjc/related?hl=en-US</li>
     <li>And click “start” to let it run.</li>
  </ul>
   <BR>
     For Collection Scraper added as prototype
     <ul>
       <li>Open your collection page like : https://www.opensea.io/collection/yourcollectionsname</li>
       <li>Set the browser's zoom to 50% or less and wait for the page to fully load. </li>
       <li>Click "SCRAPE Collection" Button to let it run</li>
       <li>If you're having trouble doing it in bulk, on the collection page search for 1 and start then 2 then 3...
          You can do this up to 9 for a 10k collection.</li>
     </ul>

 
# Checklist before press "start" button
 <p><ul>
   <li>Disabled opensea night mode</li>
   <li>Opensea collection link must end with "assets/create", <BR>
     look like this : https://www.opensea.io/collection/yourcollectionsname/<B>assets/create</b></li>
  <li>If polygon please tick "polycon blockchain</li>
  <li>Please check "complete listing" for listing and unchecked for create NFT without listing step</li>
  <li>If polygon please tick "polycon blockchain!</li>
  <li>Select your images & json "src" folder</li>
   <li>double check your image / json format: 1.png or 1.json</li>
   </ul>
  </p>

# ChromeDriver - WebDriver for Chrome	
Download your compatible chromedriver.exe https://chromedriver.chromium.org/downloads
     
# Enhanced section
Will do a unique price setting for each individual nft image. <BR>
If you like my project, please check out my NFTs https://opensea.io/collection/fortune-cat-neko and do a minimun support.
Thank you.
     
# Message for a MacOS user
Currently this script only tested in Windows 7. Not compatible for MacOS

# Contact me
If you have any questions or want to get in contact you can find me on twitter by searching @klvntss

# Thanks
Please share and leave your star star<BR>
If you found it useful, buy me a coffee( i like coffee :), <BR>
Paypal: https://paypal.me/klvntss<BR>
Ethereum address: <B>0xd5146965809e4286e24dcf2bfbf58c3840d433a2</b><BR>
Thank you very much </p>
