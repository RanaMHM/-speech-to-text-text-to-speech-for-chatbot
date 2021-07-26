 # Speech to text - STT
<br>

*   Through [The IBM Cloud catalog](https://cloud.ibm.com/catalog), the speech-to-text conversion service is selected then the special page will be opened and from here the region has been changed to Dallas and next click on **Create** <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img width="743" alt="region" src="https://user-images.githubusercontent.com/52053143/127054230-6baa36ee-ba39-4ff5-883a-83318f2091fc.png">

<br><br>

*   We open the **service credentials** and we will need both an **APIKEY** and h786f  for later use. <br>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img width="938" alt="1" src="https://user-images.githubusercontent.com/52053143/127054262-efa3ec9f-7380-43cb-97c5-e48008f558aa.png">
<br>

 *   Then the codes were downloaded from [watson-streaming-stt](https://github.com/IBM/watson-streaming-stt) and opened by Visual Studio Code and made some modifications such as changing the **APIKEY** and region with following the steps in this video.   [▶](https://www.youtube.com/watch?v=YCyuZM454_I) 


<br><br>



  ## Additions: The following code has been added to save the converted speech to text in a special file. 

  > **` with open('output.txt' ,'w') as out:out.writelines(data['results'][0]['alternatives'][0]['transcript'])`** 
 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img width="960" alt="STT" src="https://user-images.githubusercontent.com/52053143/127054334-46a312b1-3c46-4f0a-91b7-e30ed6476a4d.png">


*  The last sentence reached by converting speech to text was saved in the file named [output.txt](https://github.com/RanaMHM/IBM-Watson-STT-TTS/blob/main/output.txt)   
<hr><br>

 # Text to Speech - TSS
 
 <br>
 
The first steps will be done as in STT, but by choosing Text-to-Speech from the catalog.
Then the steps in this video are followed [⊵](https://www.youtube.com/watch?v=8k8S5ruFAUs) and work on the codes by choosing the appropriate language and changing the voice and writing the speech we want to convert.
