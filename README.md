
# bulk-upload-to-opensea
A cross platform python IDE implementing selenium 4<BR>
If you want to support this project or me, please check out my NFTs <BR>
https://opensea.io/collection/fortune-cat-neko and wish give it a little love or grab it.<BR>
Thank you.

  Tutorial video
  https://www.youtube.com/watch?v=yEowEDfTSpA
  
# INSTRUCTIONS
<ul>
  <li>Download and extract this project in your local device (keep all files and folders that come with the repo in this folder)</li>
  <li>Download and update Python. My python version is 3.8.10 * https://www.youtube.com/watch?v=9o4gDQvVkLU</li>
   <li>Copy Chrome profile into Chrome profile that come with the repo in this folder<BR>
     search "%LOCALAPPDATA%\Google\Chrome\User Data\" copy chrome profile. <BR>
     https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/
</li>
   <li>Put all the NFTs images into folder “src/images” (etc 1.png), and NFTs properties metadata .json file put into folder src/json. (etc 1.json)</li>
   <li>Open this project folder with any code editor and click "open powershell " or ‘Terminal’</li>
   <li>Pip install requirements.txt by running the following command (pip install -r requirements.txt) </li>
   <li>Run the script, type “python upload.py”</li>
   <li>Once running the script, will pop-up a dialog box / application </li>
   <li>Fill in the variable for your project upload properties, </li>
     <ul>
       <li>Opensea collection link: https://www.opensea.io/collection/yourcollectionsname/assets/create</li>
        <li>Start number 1</li>
        <li>End number 999 or any number</li>
        <li>Default price: 0.005</li>
        <li>Title with end “#” symbol</li>
        <li>Description</li>
        <li>NFT image format "png"</li>
        <li>External link start with http….</li>
     </ul>
   <li>Click and Select the “src” folder.</li>
   <li>Click and “save this form”</li>
     <li>Click “open chrome browser” will popup new chrome browser, login / sign-in your metamask account. Download metamask extension if don’t have</li>
     <li>And click “start” to let it run.</li>
  </ul>


# File usage
For slow internet speed, please use general file ** xxxx.py**<BR>
For speed up the upload process, please use **xxx-fast.py**<BR>
For some user have "SSL: CERTIFICATE_VERIFY_FAILED" issue, please use **xxx-SSL.py**<BR>
For only listing, please use **xxx-only.py**  <BR>

     
# Checklist before press "start" button
 <p><ul>
   <li>Disabled opensea night mode</li>
   <li>You local / PC Chrome profile are copy into the folder "chrome_profile"</li>
   <li>Opensea collection link must end with "assets/create", <BR>
     look like this : https://www.opensea.io/collection/yourcollectionsname/assets/create</li>
   <li>untick "polycon blockchain</li>
   <li>Select "src" folder</li>
   <li>double check your image / json format: 1.png or 1.json</li>
   <li>press "open chrome browser" button, will popup a new chrome browser</li> 
   </ul>
     </p>

#files
  
# Error message indicator
DeprecationWarning: use options instead of chrome_options chrome_options=opt,
<ul><li>1) Press "open chrome browser" and 2) "start" button to resolved this error message</li></ul>
urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]   
<ul><li>please use "upload-ssl.py" this file</li></ul>
     
# Enhanced section
Will do a unique price setting for each individual nft image. <BR>
If you like my project, please check out my NFTs https://opensea.io/collection/fortune-cat-neko and do a minimun support.
Thank you.
     
# Message for a MacOS user
Currently this script only tested in Windows 7. You can try run into your MacOS
and feedback to us. Thank you

If you have any questions or want to get in contact you can find me on twitter by searching @klvntss

# Thanks
Please share and leave your star star<BR>
If you found it useful, buy me a coffee( i like coffee :), here is my Ethereum address: <B>0xd5146965809e4286e24dcf2bfbf58c3840d433a2</b><BR>
Thank you very much </p>
